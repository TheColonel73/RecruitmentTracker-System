CREATE TABLE `contact` (
  `idcontact` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `telephone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dateadded` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idcontact`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `job` (
  `idjob` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` mediumtext,
  `location` varchar(100) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `idcontact` int(11) NOT NULL,
  PRIMARY KEY (`idjob`),
  KEY `idcontact_idx` (`idcontact`),
  CONSTRAINT `idcontact` FOREIGN KEY (`idcontact`) REFERENCES `contact` (`idcontact`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
