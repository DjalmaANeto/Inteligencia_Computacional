Perceptron brain;

Point[] points = new Point[100];

int traningIndex = 0;

void setup() {
  size (500, 500);
  //inicializando o Perceptron
  brain = new Perceptron(3);  
  //inicializando os pontos 
  for (int i = 0; i< points.length; i++) {
    points[i] = new Point();
  }

  /*
  float[] inputs = {-1, 0.5};
  int guess = brain.guess(inputs);
  println(guess);
  */
  
}

void draw() {
  background(255);
  stroke(0);
  Point p1 = new Point(-1,f(-1));
  Point p2 = new Point(1,f(1));
  line(p1.pixelx(), p1.pixely(), p2.pixelx(), p2.pixely());
  
  Point p3 = new Point(-1, brain.guessY(-1));
  Point p4 = new Point(1, brain.guessY(1));
  line(p3.pixelx(), p3.pixely(), p4.pixelx(), p4.pixely());
  
  for (Point pt : points) {
    pt.show();
  }

  for (Point pt : points) {
    float[] inputs = {pt.x, pt.y, pt.bias};
    int target = pt.label; 
    int guess = brain.guess(inputs);
    if (guess == target) {
      fill(0, 255, 0);
    } else {
      fill(255, 0, 0);
    }
    noStroke();
    ellipse(pt.pixelx(), pt.pixely(), 8, 8);
  }
    Point traning = points[traningIndex]; 
    float[] inputs = {traning.x, traning.y, traning.bias};
    int target = traning.label;
    brain.train(inputs, target);
    traningIndex++;
    if(traningIndex == points.length){
      traningIndex = 0;
    }
}
