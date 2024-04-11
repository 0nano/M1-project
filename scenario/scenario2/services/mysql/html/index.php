<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Connexion - Exemple non sécurisé</title>
</head>
<body>

<h2>Connexion - Exemple non sécurisé</h2>

<form action="login.php" method="post">
    <label for="username">Nom d'utilisateur :</label>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Mot de passe :</label>
    <input type="password" id="password" name="password" required><br><br>
    <input type="submit" value="Se connecter">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les données du formulaire
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Connexion à la base de données MySQL (Attention: connexion sans mot de passe)
    $mysqli = new mysqli('localhost', 'root', '', 'mydatabase');

    // Vérifier la connexion
    if ($mysqli->connect_errno) {
        echo "Échec de la connexion à MySQL : (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
        exit;
    }

    // Exécuter une requête SQL (vulnérable à l'injection SQL)
    $sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    $result = $mysqli->query($sql);

    // Vérifier si l'utilisateur existe
    if ($result->num_rows > 0) {
        echo "Connexion réussie ! Bienvenue, $username.";
    } else {
        echo "Identifiants incorrects. Veuillez réessayer.";
    }

    // Fermer la connexion
    $mysqli->close();
}
?>

</body>
</html>