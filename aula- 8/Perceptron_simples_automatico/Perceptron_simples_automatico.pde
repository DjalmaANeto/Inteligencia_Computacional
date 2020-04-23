Perceptron brain;

Point[] points = new Point[100];

int traningIndex = 0;

void setup() {
  size (500, 500);
  //inicializando o Perceptron
  brain = new Perceptron();  
  //inicializando os pontos 
  for (int i = 0; i< points.length; i++) {
    points[i] = new Point();
  }

  float[] inputs = {-1, 0.5};
  int guess = brain.guess(inputs);
  println(guess);
}

void draw() {
  background(255);
  stroke(0);
  line(0, 0, width, height);
  for (Point pt : points) {
    pt.show();
  }

  for (Point pt : points) {
    float[] inputs = {pt.x, pt.y};
    int target = pt.label;
   // brain.train(inputs, target); 
    int guess = brain.guess(inputs);
    if (guess == target) {
      fill(0, 255, 0);
    } else {
      fill(255, 0, 0);
    }
    noStroke();
    ellipse(pt.x, pt.y, 8, 8);
  }
    Point traning = points[traningIndex]; 
    float[] inputs = {traning.x, traning.y};
    int target = traning.label;
    brain.train(inputs, target);
    traningIndex++;
    if(traningIndex == points.length){
      traningIndex = 0;
    }
}

/*
void mousePressed(){
  for (Point pt : points) {
  }
}
*/
