0x14. MySQL
DevOps - SysAdmin - MySQL

## Task 0: Install MySQL
- MySQL distribution must be 5.7.x.
- Ensure task #3 of your SSH project is completed for web-01 and web-02.
- Please make sure you have your README.md pushed to GitHub.
## Task 1: Let us in!
- Create a MySQL user named holberton_user on both web-01 and web-02.
- Provide access to check the primary/replica status of your databases.
- Ensure task #3 of your SSH project is completed for web-01 and web-02.

## Task 2: If only you could see what I've seen with your eyes
- Create a database named tyrell_corp.
- Create a table named nexus6 and add at least one entry.
- Ensure holberton_user has SELECT permissions on the table.

## Task 3: Quite an experience to live in fear, isn't it?
- Create a new user for the replica server on web-01.
- Set the name of the new user as replica_user with the host name set to %.
- Ensure appropriate permissions for replica_user to replicate the primary MySQL server.
- Ensure holberton_user has SELECT privileges on the mysql.user table.


## Task 4: Setup a Primary-Replica infrastructure using MySQL
- Host MySQL primary on web-01, comment out the bind-address parameter.
- Host MySQL replica on web-02.
- Setup replication for the MySQL database named tyrell_corp.


## Task 5: MySQL backup
- Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
- Ensure the dump contains all MySQL databases.
- Compress the dump to a tar.gz archive with a specific format.
- The script accepts a password argument for MySQL connection.

- Directory: 0x14-mysql
- File: 5-mysql_backup
