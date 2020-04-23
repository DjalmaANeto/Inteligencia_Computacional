

class Perceptron {
  //variavel pesos 
  float[] weights = new float[2];
  //variavel learn rate ou taxa de aprendizagem 
  float lr = 0.1;
  //construtor de perceptrons 
  Perceptron() {
    //inicializando os pesos de forma aleatoria
    for (int i = 0; i < weights.length; i++) {
      weights[i] = random(-1, 1);
    }
  }

  //função de ativação 
  int sign(float n) {
    if (n >= 0) {
      return 1;
    } else {
      return -1;
    }
  }

  int guess(float[] inputs) {
    float sum = 0; 
    for (int i = 0; i < weights.length; i++) {
      sum += inputs[i] * weights[i];
    }
    int output = sign(sum);
    return output;
  }

  void train(float[] inputs, int target) {
    int guess = guess(inputs);
    int error = target - guess;
    //corrigindo todos os erros     
    for (int i = 0; i < weights.length; i++) {
      weights[i] += error * inputs[i] * lr;
    }
  }
}
