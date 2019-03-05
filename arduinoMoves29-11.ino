#include <Servo.h>

//////////////// SMARA - ROCCASALVO - CONTURSO - RUBIK SOLVER - //////////////////////


int angle = 90;

int Frontangle=0,Backangle=0,Upangle=0,Downangle=0,Rightangle=0,Leftangle=0; //For horario moves
int frontangle=0,backangle=0,upangle=0,downangle=0,rightangle=0,leftangle=0;//For antihorario moves
int F2angle=0,B2angle=0,U2angle=0,D2angle=0,R2angle=0,L2angle=0;            // For double moves

Servo servoArm;
Servo servoBase;

char inByte;
String Str = "";

void setup () {

  Serial.begin(9600);
  Serial.println("p");
  servoArm.attach(3);
  servoBase.attach(4);
  servoArm.write(180);
  delay(500);
  servoBase.write(90);



}



////////Basic Movements////////

void Push1() {

  delay(1000);
  servoArm.write(109);
  delay(1500);
  servoArm.write(115);
  delay(300);
  servoArm.write(120);
  delay(500);
  servoArm.write(125);
  delay(500);
  servoArm.write(180);
  delay(1000);

}

void Push() {

  delay(1000);
  servoArm.write(109);
  delay(1500);
  servoArm.write(115);
  delay(300);
  servoArm.write(120);
  delay(500);
  servoArm.write(125);
  delay(500);
  servoArm.write(180);
  delay(1000);

}
void Rotate(int grades) {

  servoBase.write(grades);
  delay(1000);

}

void Wait(int ms) {

  delay(ms);

}

void Hold() {

  servoArm.write(160.2);
  delay(500);

}

void Release() {

  servoArm.write(180);
  delay(500);

}

/////////////////////////////

////////// Color Detection /////////////////

void ColorDetection() {

  // Serial.println("RIGHT");
  Rotate(15);
  Wait(3000);

  //Serial.println("DOWN"); //Si no anda es porq antes picaba por el time del print
  Rotate(171);
  Wait(1000);
  Push1();
  Rotate(90);
  Wait(3000);

  //Serial.println("UP");
  Rotate(171);
  for (int i = 0; i <= 1; i++) {
    Push1();
  }
  Rotate(90);
  Wait(10500);

  //Serial.println("LEFT");
  Push1();
  Wait(10000);

  //Serial.println("BACK");
  Push1();
  Push1();

  Rotate(90);
  Wait(10500);

  //Serial.println("FRONT"); ///Return to front face
  Push1();
  Push1();
  Rotate(90);
  angle = 90;

}




void ConvertRedPoss(int faceangle)
{
    if (faceangle == 90)
  {
    angle = 90;
  }
  else if (faceangle == 1)
  {
    angle = 0;
  }
  else if (faceangle == 180)
  {
    angle = 180;
  }
}


void FF() {

  if (angle == 90) {
    Rotate(15);
    Push();
    Hold();
    Rotate(82);
    Release();
    Push();
    Push();
    Push();
    Rotate(171);
    Frontangle = 180;
    Wait(2000);

  }

  if (angle == 0) {

    Rotate(90);
    Push();
    Push();
    Push();
    Hold();
    Rotate(180);
    Release();
    Push();
    Rotate(90);
    Frontangle = 90;
    Wait(2000);

  }

  if (angle == 180) {
    Rotate(90);
    Push();
    Hold();
    Rotate(180);
    Release();
    Push();
    Push();
    Rotate(90);
    Push();
    Rotate(180);
    Push();
    Frontangle = 180;
  }

ConvertRedPoss(Frontangle);

}

void ff(){
  if (angle == 90) {
    Rotate(15);
    Push();
    Rotate(90);
    Hold();
    Rotate(6);
    Release();
    Rotate(90);
    Push();
    Rotate(171);
    frontangle = 180;
    Wait(2000);
  }

    if (angle == 0) {
    Rotate(90);
    Push();
    Push();
    Push();
    Hold();
    Rotate(6);
    Release();
    Rotate(90);
    Push();
    Rotate(15);
    Push();
    frontangle = 1;
    Wait(2000);
  }

    if (angle == 180) {
    Rotate(90);
    Push();
    Hold();
    Rotate(6);
    Release();
    Push();
    Push();
    Push();
    Rotate(90);

    frontangle = 90;
  }
  
ConvertRedPoss(frontangle);
}
void F2(){

 if (angle == 90) {
    Rotate(15);
    Push();
    Hold();
    Rotate(180);
    Release();
    Rotate(90);
    Push();
    Rotate(15);
    Push();
    F2angle = 1;
    Wait(2000);

  }

  if (angle == 0) {

    Rotate(90);
    Push();
    Push();
    Push();
    Rotate(15);
    Hold();
    Rotate(180);
    Release();
    Push();
    Rotate(90);
    Push();
    Push();
    Rotate(90);
    F2angle = 90;
    Wait(2000);

  }

  if (angle == 180) {
    Rotate(90);
    Push();
    Rotate(15);
    Hold();
    Rotate(180);
    Release();
    Push();
    Rotate(90);
    Push();
    F2angle = 90;
  }

ConvertRedPoss(F2angle);

}

  
}
void B() {

  if (angle == 90) {

    Rotate(15);
    Push();
    Hold();
    Rotate(82);
    Release();
    Rotate(171);
    Push();
    Rotate(90);
    Push();
    Push();
    Push();

    Backangle = 90;
    Wait(2000);

  }

  if (angle == 0) {
    Rotate(90);
    Push();
    Push();
    Push();
    Hold();
    Rotate(180);
    Release();
    Push();
    Rotate(90);
    Backangle = 90;
    Wait(2000);

  }



  if (angle == 180) {
    Rotate(90);
    Push();
    Push();
    Push();
    Hold();
    Rotate(180);
    Release();
    Rotate(90);
    Push();
    Rotate(180);
    Push();
    Backangle = 180;
    Wait(2000);
  }
ConvertRedPoss(Backangle);
}

void b(){
    if (angle == 90) {
    Rotate(171);
    Push();
    Rotate(90);
    Hold();
    Rotate(6);
    Release();
    Push();
    Rotate(90);
    Push();
    backangle = 90;
    Wait(2000);

  }

  if (angle == 0) {
    Rotate(90);
    Push();
    Rotate(171);
    Hold();
    Rotate(82);
    Release();
    Push();
    Rotate(90);
    Push();
    backangle = 90;
    Wait(2000);

  }



  if (angle == 180) {
    Rotate(90);
    Push();
    Push();
    Push();
    Hold();
    Rotate(180);
    Release();
    Rotate(90);
    Push();
    Rotate(180);
    Push();
    backangle = 180;
    Wait(2000);
  }
  ConvertRedPoss(backangle);
}
void U() {

  if (angle == 90) {

    Push();
    Push();
    Hold();
    Rotate(180);
    Release();
    Push();
    Push();
    Upangle = 180;
    Wait(2000);

  }

  if (angle == 0) {
    Push();
    Push();
    Hold();
    Rotate(82);
    Release();
    Push();
    Push();
    Upangle = 90;
    Wait(2000);

  }

  if (angle == 180) {
    Push();
    Push();
    Rotate(90);
    Hold();
    Rotate(180);
    Release();
    Push();
    Push();
    Rotate(90);
    Upangle=90;
    Wait(2000);
  }

ConvertRedPoss(Upangle);
}
void u(){
  
  if (angle == 90) {

    Push();
    Push();
    Hold();
    Rotate(6);
    Release();
    Push();
    Push();
    upangle = 1;
    Wait(2000);

  }

  if (angle == 0) {
    Push();
    Push();
    Rotate(90);
    Hold();
    Rotate(6);
    Release();
    Push();
    Push();
    Rotate(90);
    upangle = 90;
    Wait(2000);

  }

  if (angle == 180) {
    Push();
    Push();
    Hold();
    Rotate(82);
    Release();
    Push();
    Push();
    upangle=90;
    Wait(2000);
  }

ConvertRedPoss(upangle);
}
void D() {




  if (angle == 90) {

    Hold();
    Rotate(180);
    Release();
    Downangle = 180;
    Wait(2000);
  }

  if (angle == 0) {

    Hold();
    Rotate(97);
    Release();
    Downangle = 90;
    Wait(2000);

  }

  if (angle == 180) {
    Rotate(15);
    Hold();
    Rotate(97);
    Release();
    Rotate(15);
    Push();
    Rotate(90);
    Push();
    Rotate(180);
    Push();
    Downangle = 180;
    Wait(2000);

  }

ConvertRedPoss(Downangle);
}
void d(){
    if (angle == 90) {

    Hold();
    Rotate(6);
    Release();
    downangle = 180;
    Wait(2000);
  }

  if (angle == 180) {

    Hold();
    Rotate(97);
    Release();
    downangle = 90;
    Wait(2000);

  }

  if (angle == 0) {
    Rotate(90);
    Hold();
    Rotate(6);
    Release();
    Push();
    Rotate(90);
    Push();
    Rotate(171);
    Push();
    downangle = 180;
    Wait(2000);
}

void L() {

  if (angle == 90) {
    Push();
    Hold();
    Rotate(180);
    Release();
    Push();
    Push();
    Push();
    Leftangle = 1;
    Wait(2000);

  }


  if (angle == 0) {
    Push();
    Hold();
    Rotate(97);
    Release();
    Push();
    Push();
    Push();
    Leftangle = 90;
    Wait(2000);

  }


  if (angle == 180) {
    Push();
    Rotate(90);
    Hold();
    Rotate(180);
    Release();
    Push();
    Rotate(90);
    Push();
    Rotate(15);
    Push();
    Leftangle = 1;
    Wait(2000);
  }

ConvertRedPoss(Leftangle);
}

void l(){
    if (angle == 90) {
    Push();
    Hold();
    Rotate(6);
    Release();
    Push();
    Push();
    Push();
    leftangle = 1;
    Wait(2000);

  }


  if (angle == 180) {
    Push();
    Hold();
    Rotate(97);
    Release();
    Push();
    Push();
    Push();
    leftangle = 90;
    Wait(2000);

  }


  if (angle == 1) {
    Push();
    Rotate(90);
    Hold();
    Rotate(6);
    Release();
    Push();
    Rotate(90);
    Push();
    Rotate(171);
    leftangle = 180;
    Wait(2000);
  }
}
void R() {

  if (angle == 90) {

    Push();
    Push();
    Push();
    Hold();
    Rotate(180);
    Release();
    Push();
    Rightangle = 180;
    Wait(2000);

  }


  if (angle == 0) {

    Push();
    Push();
    Push();
    Hold();
    Rotate(97);
    Release();
    Push();
    Rightangle = 90;
    Wait(2000);

  }


  if (angle == 180) {

    Push();
    Push();
    Push();
    Rotate(90);
    Hold();
    Rotate(180);
    Release();
    Push();
    Rotate(90);
    Push();
    Rotate(15);
    Push();
    Push();
    Rightangle = 1;
    Wait(2000);

  }
ConvertRedPoss(Rightangle);
}

void r(){
    if (angle == 90) {

    Push();
    Push();
    Push();
    Hold();
    Rotate(6);
    Release();
    Push();
    rightangle = 1;
    Wait(2000);

  }


  if (angle == 180) {

    Push();
    Push();
    Push();
    Hold();
    Rotate(97);
    Release();
    Push();
    rightangle = 90;
    Wait(2000);

  }


  if (angle == 1) {

    Push();
    Push();
    Push();
    Rotate(90);
    Hold();
    Rotate(6);
    Push();
    Rotate(90);
    Push();
    Rotate(171);
    Push()
    Push();
    rightangle = 180;
    Wait(2000);
}

void loop() {


  if ( Serial.available() > 0 )
    inByte = Serial.read();//
  Serial.println(inByte);



  // ReadColors

  if ( inByte == 'S') { //Start Detection
    ColorDetection();
  }

  if ( inByte == 'F') {
    FF();
  }



  if ( inByte == 'B') {
    B();

  }

  if (inByte == 'U') {

    U();


  }

  if ( inByte == 'D') {

    D();


  }

  if ( inByte == 'L') {

    L();

  }


  if ( inByte == 'R') {

    R();

  }


  ///////////Invert Movements/////////////

  if ( inByte == 'f'){
    
       ff();
     }



       if( inByte == 'b'){
       b();

     }

       if (inByte == 'u') {

       u();


     }

       if( inByte == 'd'){

       d();


     }

       if( inByte == 'l'){

       l();

     }


       if( inByte == 'r'){

       R();

     }

     ///////////////////////Doble Giro///////////////////////

     
  if ( inByte == '1'){
    
       F2();
     }



       if( inByte == '2'){
       B2();

     }

       if (inByte == '3') {

       U2();


     }

       if( inByte == '4'){

       D2();


     }

       if( inByte == 'L2'){

       L2();

     }


       if( inByte == 'R2'){

       R2();

     }
     }
