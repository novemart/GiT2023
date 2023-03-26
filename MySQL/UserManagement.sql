create user 'martina1'@'localhost' identified by 'password';

grant select on Company.* to 'martina1'@'localhost';

grant insert on Company.* to 'martina1'@'localhost';

revoke insert on Company.* from 'martina1'@'localhost';
