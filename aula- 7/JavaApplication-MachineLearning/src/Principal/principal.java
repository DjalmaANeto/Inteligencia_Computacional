/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Principal;

import classes.DadosRegressao;
import classes.RegressaoLinear;
import java.util.ArrayList;

/**
 *
 * @author Djalma
 */
public class principal {

    public static void main(String[] args) {

        ArrayList<DadosRegressao> dadosRegressao = new ArrayList<>();
        dadosRegressao.add(new DadosRegressao(1, 1));
        dadosRegressao.add(new DadosRegressao(2, 2));
        dadosRegressao.add(new DadosRegressao(3, 3));

        RegressaoLinear r = new RegressaoLinear(dadosRegressao);

        System.out.println("Theta0 = " + r.getT0() + ", Theta1 = " + r.getT1());

        r.calcularGradientDescent();

        System.out.println("Theta0 = " + r.getT0() + ", Theta1 = " + r.getT1());

        System.out.println(r.retornarPredicao(4));

        // 50 = Theta0 = 0.3258122859586933, Theta1 = 0.7990099679934095
        // 200 = Theta0 = 0.28977305529372266, Theta1 = 0.8725172785941928
        // 1000 = Theta0 = 0.11071520925847289, Theta1 = 0.9512961894220736
        // 2000 = Theta0 = 0.03325724402174409, Theta1 = 0.9853700812740419
        // 2000 (0,02) = Theta0 = 0.0029921703047745517, Theta1 = 0.9986837391473431
    }

}
