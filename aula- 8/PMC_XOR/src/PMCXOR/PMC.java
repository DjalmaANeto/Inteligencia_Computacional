package PMCXOR;

import java.util.Random;

/*
 o plicativo funcionara com três neuronios para a formulação do perceptron 
multiplas camadas, cada neuronio possuira uma entrada extra que sera definda 
como bias. Para a aprimeira geração todos os pesos serão atualizados com pesos 
aleatorios entre 0 e 1 e serão atualizados sempre que não atingirem o resultado
desejado. 
 */

/**
 * @author Aluno
 */
public class PMC {

    
    public static void main(String[] args) {
        //array representando a tabelaverdade XOR 
        double[][] arrayXOR = {{1,1,0},
                               {1,0,1},
                               {0,1,1},
                               {0,0,0}
                               };
        //pesos para atribuição aleatória
        double w1X1;
        double w2X1;
        double w1X2;
        double w2X2;
        double w1Y1;
        double w1Y2;
        double wBias1;
        double wBias2;
        double wBias3;
        
        //fator de aprendizagem
        double fatorAprendizagem = 0.5; 
        
        //definição de variaveis 
        //tres erros:
        double erroDelta3 = 0;
        double erroDelta2 = 0;
        double erroDelta1 = 0;
        //resultados das ativações:
        double y1 = 0;
        double y2 = 0;
        double y3 = 0;
        int fila = 0;//esta int fila é percorrida 4 vezes gerando a tabela xor (array)
        //gerações interações ou vidas:
        int interacoes = 1;
        
        //ciclo que percorreas 4 filas do array XOR 
        while(fila <=3 ){
            //setando 0 para variaveis fazerem oscalculos desde o inicio 
            y1 = 0;
            y2 = 0;
            y3 = 0;
            erroDelta3 = 0;
            erroDelta2 = 0;
            erroDelta1 = 0;
            interacoes = 0;
            
            //setando valores aleatorios entre 0 e 1 a todos os pesos
            w1X1= new Random().nextDouble();
            w2X1= new Random().nextDouble();
            w1X2= new Random().nextDouble();
            w2X2= new Random().nextDouble();
            w1Y1= new Random().nextDouble();
            w1Y2= new Random().nextDouble();
            wBias1= new Random().nextDouble();
            wBias2= new Random().nextDouble();
            wBias3= new Random().nextDouble();
            
            //ciclo que controlara quantas gerações ira acontecer o treinamento
            while(interacoes <= 1000){
                //calculando a saida da camada oculta de neuronios 
                y1 = (arrayXOR[fila][0]*w1X1) + (arrayXOR[fila][1]*w1X2)+(1*wBias1);
                y2 = (arrayXOR[fila][0]*w2X1) + (arrayXOR[fila][1]*w2X2)+(1*wBias2);
                
                //implementa a funçao sigmoide de ativação
                y1 = 1.0/(1 + Math.pow(Math.E, (-1)* y1));
                y2 = 1.0/(1 + Math.pow(Math.E, (-1)* y2));
                
                //calcula a saida do neuronio de saida
                y3 = (y1 * w1Y1) + (y2 * w1Y2) + (1 * wBias3);
                //implementa a funcao sigmoide 
                y3 = 1.0/(1 + Math.pow(Math.E, (-1) * y3));
                
                //MOMENTO DA BACKPROPAGATION
                erroDelta3 = (y3 * (1 - y3)) * (arrayXOR[fila] [2] - y3);
                
                //Ajustando os pesos do neoronio de saida 
                w1Y1 = w1Y1 + (fatorAprendizagem * erroDelta3 * y1);
                w1Y2 = w1Y2 + (fatorAprendizagem * erroDelta3 * y2);
                wBias3 = wBias3 + (erroDelta3);
                
                //calaculo de erro da camada oculta de neoronios
                erroDelta1 = (y1 * (1 - y1)) * erroDelta3 - w1Y1;
                erroDelta2 = (y2 * (1 - y2)) * erroDelta3 - w1Y2;
                
                //ajusta os pesos da camada oculta (neoronio 1)
                w1X1 = w1X1 + (fatorAprendizagem * erroDelta1 * arrayXOR[fila] [0]); 
                w1X2 = w1X2 + (fatorAprendizagem * erroDelta1 * arrayXOR[fila] [1]);
                wBias1 = wBias1 + erroDelta1;
                
                //ajusta os pesos da camada oculta (neurona 2)
                w2X1 = w2X1 + (fatorAprendizagem * erroDelta2 * arrayXOR[fila] [0]); 
                w2X2 = w2X2 + (fatorAprendizagem * erroDelta2 * arrayXOR[fila] [1]);
                wBias2 = wBias2 + erroDelta2;
                
                interacoes++;
            }
            
            //imprimindo cada fila de arrays XOR quando terminado o treino
            System.out.println(""+(int)arrayXOR[fila][0]+"\tXOR\t"+(int)arrayXOR[fila][1]+"\t=\t"+(int)arrayXOR[fila][2]);
            fila++;
        }
    }
}
    

