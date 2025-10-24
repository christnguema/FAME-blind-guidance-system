using Plugin.BLE;
using Plugin.BLE.Abstractions.Contracts;
using Plugin.BLE.Abstractions.EventArgs;
using System;
using System.Threading.Tasks;
using Microsoft.Maui.Media;
using Microsoft.Maui.Devices; //  Pour la vibration


namespace BlindAssistant
{
    public partial class MainPage : ContentPage
    {
        // UUIDs du service et de la caractéristique
        readonly Guid ServiceUuid = Guid.Parse("12345678-1234-5678-1234-56789abcdef0");
        readonly Guid CharacteristicUuid = Guid.Parse("abcdef01-1234-5678-1234-56789abcdef0");

        readonly IBluetoothLE ble;
        readonly IAdapter adapter;

        private DateTime lastSpeechTime = DateTime.MinValue;
        private ushort lastDistance = 0;


        public MainPage()
        {
            InitializeComponent();

            _ = SpeakAsync("Bonjour, système de guidage prêt !");
            ble = CrossBluetoothLE.Current;
            adapter = CrossBluetoothLE.Current.Adapter;
            adapter.DeviceDiscovered += OnDeviceDiscovered;
        }

        //------ 0. Synthèse vocale ------
        public async Task SpeakAsync(string message)
        {
            try
            {
                await TextToSpeech.Default.SpeakAsync(message);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Erreur TTS : {ex.Message}");
            }
        }

        // ---- 1. Bouton "Scanner" ----
        private async void OnScanClicked(object sender, EventArgs e)
        {
            await SpeakAsync("Début du scanne Bluetooth !");
            try
            {
                await Permissions.RequestAsync<Permissions.LocationWhenInUse>();

                if (!ble.IsOn)
                {
                    await DisplayAlert("Bluetooth", "Active le Bluetooth avant de continuer.", "OK");
                    return;
                }

                DistanceLabel.Text = "🔄 Recherche du capteur...";
                await adapter.StartScanningForDevicesAsync();
            }
            catch (Exception ex)
            {
                await DisplayAlert("Erreur", ex.Message, "OK");
            }
        }

        // ---- 2. Quand un périphérique est trouvé ----
        private void OnDeviceDiscovered(object sender, DeviceEventArgs e)
        {
            if (e.Device.Name?.Contains("HC_SR04_Sensor") == true)
            {
                _ = ConnectToDeviceAsync(e.Device);
            }
        }

        // ---- 3. Connexion et réception ----
        private async Task ConnectToDeviceAsync(IDevice device)
        {
            try
            {
                await adapter.StopScanningForDevicesAsync();
                MainThread.BeginInvokeOnMainThread(() =>
                    DistanceLabel.Text = $"Connexion à {device.Name}..."
                );

                await adapter.ConnectToDeviceAsync(device);
                var service = await device.GetServiceAsync(ServiceUuid);
                var characteristic = await service.GetCharacteristicAsync(CharacteristicUuid);

                if (characteristic == null)
                    throw new Exception("Caractéristique introuvable.");

                characteristic.ValueUpdated += OnValueUpdated;
                await characteristic.StartUpdatesAsync();

                MainThread.BeginInvokeOnMainThread(() =>
                    DistanceLabel.Text = "✅ Connecté. En attente de données..."
                );
                await SpeakAsync("Capteur connecté. En attente de mesures.");
            }
            catch (Exception ex)
            {
                MainThread.BeginInvokeOnMainThread(() =>
                    DistanceLabel.Text = $"❌ Erreur : {ex.Message}"
                );
                MainThread.BeginInvokeOnMainThread(() =>
                    _ = SpeakAsync("Erreur de connexion au capteur.")
                );
            }
        }

        // ---- 4. Quand une mesure est reçue ----
        private void OnValueUpdated(object sender, CharacteristicUpdatedEventArgs e)
        {
            try
            {
                var data = e.Characteristic.Value;
                if (data == null || data.Length < 6)
                    return;

                ushort distance = BitConverter.ToUInt16(data, 0);
                uint timestamp = BitConverter.ToUInt32(data, 2);

                MainThread.BeginInvokeOnMainThread(() =>
                {
                    DistanceLabel.Text = $"Distance : {distance} cm";
                    TimestampLabel.Text = $"Reçu à : {DateTimeOffset.FromUnixTimeSeconds(timestamp):HH:mm:ss}";
                });

                HandleFeedback(distance);
            }
            catch (Exception ex)
            {
                MainThread.BeginInvokeOnMainThread(() =>
                    DistanceLabel.Text = $"Erreur lecture : {ex.Message}"
                );
            }
        }

        // ---- 5. Logique de vibration + synthèse vocale ----
        private async void HandleFeedback(ushort distance)
        {
            // Ne pas parler trop souvent (toutes les 2 secondes minimum)
            if ((DateTime.Now - lastSpeechTime).TotalSeconds < 2)
                return;

            string message = null;

            if (distance <= 30)
            {
                message = "Attention ! Obstacle très proche.";

                //  Vibration forte pour alerter l’utilisateur
                if (Vibration.Default.IsSupported)
                {
                    try
                    {
                        // Vibration de 800 ms
                        Vibration.Default.Vibrate(TimeSpan.FromMilliseconds(800));
                    }
                    catch (FeatureNotSupportedException)
                    {
                        Console.WriteLine("Vibration non supportée sur cet appareil.");
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Erreur vibration : {ex.Message}");
                    }
                }
            }
            else if (distance <= 70)
            {
                message = $"Obstacle à {distance} centimètres.";
            }
            else if (distance <= 150 && Math.Abs(distance - lastDistance) > 20)
            {
                message = $"Obstacle détecté à environ {distance} centimètres.";
            }
            else if (distance > 150 && lastDistance <= 150)
            {
                message = "Zone dégagée.";
            }

            if (message != null)
            {
                lastSpeechTime = DateTime.Now;
                lastDistance = distance;
                await SpeakAsync(message);
            }
        }

    }
}
