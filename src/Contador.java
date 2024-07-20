import java.util.Scanner;

public class Contador {
    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite o primeiro parametro.");
		int parametroUm = scanner.nextInt();
		System.out.println("Escreve o número do segundo parâmetro");
		int parametroDois = scanner.nextInt();
		
		try {
			contar(parametroUm, parametroDois);
    	} catch (ParametrosInvalidosException exception) {
    		System.out.println("O segundo parâmetro deve ser maior que o primeiro");
    	}
    	
    }
    
	static void contar(int parametroUm, int parametroDois) throws ParametrosInvalidosException{
    	if (parametroUm >= parametroDois) {
    		throw new ParametrosInvalidosException();
    	} else {
    		int contagem = parametroDois - parametroUm;
    		for(int i = 0; i < contagem; i++) {
    			System.out.println("Imprimindo o numero " + (i+1));
    		}
    	}
    }
}      

