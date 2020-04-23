float f(float x){
  //this represents y = mx + b
  return -0.3 * x - 0.2;
}

class Point {
  float x;
  float y;
  float bias = 1; 
  int label;
  
  Point(float x_, float y_){
    x = x_;
    y = y_;
  } 
  
  //construtor de pontos 
  Point(){
    x = random(-1,1);
    y = random(-1,1);
    bias = 1;
    
    float liney = f(x);
    
    if(y > liney){
      label = 1;
    } else {
      label = -1;
    }
  }
  
  float pixelx(){
    return map(x,-1, 1, 0, width);
  }
  
  float pixely(){
    return map(y,-1, 1, height, 0);
  }
  
  void show(){
    stroke(0);
    if(label == 1){
      fill(255);
    }else{
      fill(0);
    }
    
    float px = pixelx();
    float py = pixely();
    ellipse(px, py, 16, 16);
  }
  
}
