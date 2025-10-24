def log(message):
#********** Docstring *************************************************************
    """Afficher du texte (str) dans la
    console et enregistre ce texte dans un fichier log."""
# **********************************************************************************
    f = open("stm32.log", "a") # Ouverture du fichier en mode "append"
    f.write(message) # Ecriture du message dans le fichier
    print(message) # Affichage du message dans la console
    f.write("\n") # Un retour à la ligne dans le fichier pour le prochain message
    f.close() # Fermeture du fichier
# ***********************************************************************************