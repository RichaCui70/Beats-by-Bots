#include <SPI.h>
#include <MFRC522.h>
#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above
byte readCard[4];
String MasterTag = "ENTER_YOUR_TAG_ID";
String tagID = "";
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SPI.begin();

  mfrc522.PCD_Init();
  delay(4);
  //Show details of PCD - MFRC522 Card Reader
  mfrc522.PCD_DumpVersionToSerial();

  Serial.println("--------------------------");
  Serial.println(" Access Control ");
  Serial.println("Scan Your Card>>");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (getID()) {
    Serial.println(tagID);
  }
}

boolean getID() {
  // Getting ready for Reading PICCs
  //If a new PICC placed to RFID reader continue
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return false;
  }

  //Since a PICC placed get Serial and continue
  if ( ! mfrc522.PICC_ReadCardSerial()) {
  return false;
  }

  tagID = "";
  // The MIFARE PICCs that we use have 4 byte UID
  for ( uint8_t i = 0; i < 4; i++) {
    //readCard[i] = mfrc522.uid.uidByte[i];
    // Adds the 4 bytes in a single String variable
    tagID.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  
  tagID.toUpperCase();
  mfrc522.PICC_HaltA(); // Stop reading
  return true;
}
