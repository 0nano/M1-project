-- Créer un utilisateur 'user1' avec un mot de passe
CREATE USER 'user1'@'%' IDENTIFIED BY 'password1';

-- Accorder tous les privilèges sur la base de données 'my-wonderful-website' à 'user1'
GRANT ALL PRIVILEGES ON `my-wonderful-website`.* TO 'user1'@'%';

-- Créer un utilisateur 'user2' avec un mot de passe
CREATE USER 'user2'@'%' IDENTIFIED BY 'password2';

-- Accorder des privilèges SELECT, INSERT, UPDATE sur la base de données 'my-wonderful-website' à 'user2'
GRANT SELECT, INSERT, UPDATE ON `my-wonderful-website`.* TO 'user2'@'%';
