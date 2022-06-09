import ddf.minim.*;

// Declaração de um objeto da classe Minim. Será utilizada para controlar os áudios do programa.
Minim gerenciador;
// Para cada áudio utilizado no software é necessário uma variável do tipo AudioPlayer.
AudioPlayer efeito;

// Indica qual imagem do sprite será desenhado.
// Quando true a img1 do sprite é desenhado.
// Quando false a img2 do sprite é desenhado.
boolean sp = false;
// Variáveis utilizadas para determinar a velocidade da translação do sprite.
// A função random é responsável por sortear um valor dentro do range dos parâmetros
float speedX = random(3, 5);
float speedY = random(3, 5);

// Variável utilizada para armazenar o tempo de execução em milissegundos
int tempo;

PImage backpic,a1,a2, a3,a4,a5,a6,a7,a8, wallpic, START;
int game, score, highscore, x, y, vertical, wallx[] = new int[2], wally[] =new int[2];
void setup() {
   backpic =loadImage("background.png");
   a1 =loadImage("a1.jpg");
   a2 =loadImage("a2.jpg");
   a3 =loadImage("a3.jpg");
   a4 =loadImage("a4.jpg");
   a5 =loadImage("a5.jpg");
   a6 =loadImage("a6.jpg");
   a7 =loadImage("a7.jpg");
   a8 =loadImage("a8.jpg");
   wallpic =loadImage("wall.png");
   START=loadImage("START.jpg");
   game = 1; score = 0; highscore = 0; x = -200; vertical = 0; 
  size(600,800);
  fill(0,0,0);
  textSize(20);  
  gerenciador = new Minim(this);
  efeito = gerenciador.loadFile("music.mp3");
  efeito.play();
}
void draw() { 
  if(game == 0) {
    imageMode(CORNER);
    image(backpic, x, 0);
    image(backpic, x+backpic.width, 0);
    x -= 5;
    vertical += 1;
    y += vertical;
    if(x == -1800) x = 0;
    for(int i = 0 ; i < 2; i++) {
      imageMode(CENTER);
      image(wallpic, wallx[i], wally[i] - (wallpic.height/2+100));
      image(wallpic, wallx[i], wally[i] + (wallpic.height/2+100));
      if(wallx[i] < 0) {
        wally[i] = (int)random(200,height-200);
        wallx[i] = width;
      }
      if(wallx[i] == width/2) highscore = max(++score, highscore);
      if(y>height||y<0||(abs(width/2-wallx[i])<25 && abs(y-wally[i])>100)) game=1;
      wallx[i] -= 6;
    }
   // image(birdpic, width/2, y);
   
    /*
    Condicional responsável por atualizar a variável sp que indica qual sprite deverá ser desenhado.
   A condição verifica se a diferença de tempo entre a última alteração e o tempo atual é maior
   que 500 milissegundos. Caso positivo ele altera o valor da variável sp.
   */
  if ((millis() - tempo) > 20) {
    tempo = millis();
    // A troca dos sprites pode ser realizada através do condicional comentado,
    // ou pela atribuição da variável com o operador ! (negação).
    sp = !sp;
    //if (sp == true) {
    //  sp = false;
    //} else {
    //  sp = true;
    //}
  }

  /*
    Desenha o sprite na janela.
   Uso do operador ternário para verificar qual imagem será desenhado
   Sintaxe: (condição)?(valor se verdadeiro):(valor se falso)
   Equivalente ao if-else que se encontra abaixo.
   */
  image((sp==true)?a1:a2, width/2, y);
 // if(sp == true) {
 //    image(a1,width/2, y);
//  } else {
   //  image(a2,width/2, y);
//  }
    
    
    text("Score: "+score, 10, 20);
  }
  else {
    imageMode(CENTER);
    image(START, width/2,height/2);
    text("High Score: "+highscore, 50, 130);
  }
}
void mousePressed() {
  vertical = -15;
  if(game==1) {
    wallx[0] = 600;
    wally[0] = y = height/2;
    wallx[1] = 900;
    wally[1] = 600;
    x = game = score = 0;
  }
}