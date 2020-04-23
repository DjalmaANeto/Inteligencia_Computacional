package newpackage_RNA;

import java.util.Random;

/**
 *
 * @author Djalma
 */
public class Perceptron {
    private int entrada[][] = new int[4][2];
    private int saida_esp[] = new int[4];
    private float p1;
    private float p2;
    private int i;
    private int j;
    private int y;
    private int acertos;
    private Random aleatorio;
    private float taxa_aprendizado;
    private float soma;
    private int erro;
    
     Perceptron()
    {
        //[1,1]
        entrada[0][0] =1;
        entrada[0][1] =1;
        //[0,1]
        entrada[1][0] =0;
        entrada[1][1] =1;
        //[0,0]
        entrada[2][0] =0;
        entrada[2][1] =0;
        //[1,0]
        entrada[3][0] =1;
        entrada[3][1] =0;
        
        saida_esp[0] = 1;
        saida_esp[1] = 0;
        saida_esp[2] = 0;
        saida_esp[3] = 0;
        
        aleatorio = new Random();
        
        p1 = aleatorio.nextFloat();
        p2 = aleatorio.nextFloat();
        
        taxa_aprendizado= (float) 0.5;
        y = 0;
        soma = 0;
        erro = 0;
        acertos = 0;
    }
     
     public void soma(int x1,int x2)
    {
        soma = x1*p1+x2*p2;

        if(soma>0.5)
            y = 1;
        else 
            y = 0;
    }
     
      public void treinar()
    {
        i = j =0;
        while(acertos<4)
        {
            while(i<4)
            {
                erro = 0;
                
                soma(entrada[i][j],entrada[i][j+1]);
                
                if(y==saida_esp[i])
                {
                    i++;
                    acertos++;
                }
                else
                {
                    acertos = 0;
                    erro = saida_esp[i]-y;
                    p1 = p1 + (taxa_aprendizado*erro*entrada[i][j]*aleatorio.nextFloat());
                    p2 = p2 + (taxa_aprendizado*erro*entrada[i][j+1]*aleatorio.nextFloat());
                }
                System.out.println("PESOS: "+p1+" / "+p2);
            }
            i = 0;
        }
       
    }
      
     public void classifica(int x1,int x2)
    {
        soma(x1,x2);
        System.out.println("ENTRADA: ["+x1+","+x2+"] = "+y);
        
    }
      
}
