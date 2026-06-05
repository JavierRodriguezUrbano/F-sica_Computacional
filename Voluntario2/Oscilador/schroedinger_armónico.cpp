#include <iostream>
#include "complex.h"
#include <cmath>
#include <fstream>
#include <iomanip>

using namespace std;


#define PI 3.141592654

int main(){
    int i,j,k, hermite=20;
    double n, y, polinomio, polinomio_antes, ayuda;
    int N=5000;//División discreta de la onda
    double h= 1.0/N; // condicion ´s=1/4´ko^2
    double x0=0.5, sigma=1.0/10;
    int nciclos=30;// nciclos de 1 a N/4=250; ponemos nciclos=30 para que el paso s sea preciso. Determinar nciclos determina s
    double kotilde=(2.0*PI*nciclos)/N;
    double stilde=1.0/(4.0*kotilde*kotilde);//
    double ese=stilde*h*h;
    double tiempo=0.5, w=200;  //con esto hago aproximadamente t=0,5  y w es frecuencia del oscilador
    double equilibrio=0.5; //parámetro de equilibrio del oscilador
    double Vtilde=h*h*w*w/4.0;
    fcomplex* Phi= new fcomplex[N+1];
    double Norma=0;
    double xmedio=0, x2medio=0, Heisenberg=0, Hmedio=0;
    fcomplex pmedio, p2medio;//Esto facilita su calculo luego <p>,<H>,<p^2>
    p2medio.i=pmedio.i=0;
    p2medio.r=pmedio.r=0;
    fcomplex* alpha= new fcomplex[N];
    fcomplex* beta= new fcomplex[N];
    fcomplex* chi= new fcomplex[N+1];

    ofstream file_prob("DatosGaussCentrada/probabilidad.txt");

    if(!file_prob){
       cout<<"Error al abrir el archivo probabilidad."<<endl;
       return 1;
    }

    ofstream file_norm("DatosGaussCentrada/norma.txt");

    if(!file_norm){
       cout<<"Error al abrir el archivo norma."<<endl;
       return 1;
    }


    ofstream file_real("DatosGaussCentrada/real.txt");

    if(!file_real){
       cout<<"Error al abrir el archivo real."<<endl;
       return 1;
    }

    ofstream file_img("DatosGaussCentrada/imaginario.txt");

    if(!file_img){
       cout<<"Error al abrir el archivo imaginario."<<endl;
       return 1;
    }

    ofstream file_x("DatosGaussCentrada/x_esperado.txt");

    if(!file_x){
       cout<<"Error al abrir el archivo x_esperado."<<endl;
       return 1;
    }

    ofstream file_p("DatosGaussCentrada/p_esperado.txt");

    if(!file_p){
       cout<<"Error al abrir el archivo p_esperado."<<endl;
       return 1;
    }

    ofstream file_H("DatosGaussCentrada/H_esperado.txt");

    if(!file_H){
       cout<<"Error al abrir el archivo H_esperado."<<endl;
       return 1;
    }

    ofstream file_Heisenberg("DatosGaussCentrada/Heisenberg_esperado.txt");

    if(!file_Heisenberg){
       cout<<"Error al abrir el archivo Heisenberg_esperado."<<endl;
       return 1;
    }






    for(i=0;i<(N+1);i++){
        if(i==0 || i==N){
            Phi[i].r=0;
            Phi[i].i=0;
            Norma+=0;
        }
        else{
            y=sqrt(w/2.0)*(i*h-equilibrio);
            //Gaussiana
            Phi[i]=Cgauss(0.0,(exp(-(i*h-x0)*(i*h-x0)/(2*sigma*sigma))));//la fase y termino de amplitud por posición 

            //Estado Estacionario general para n  comentar con /**/
            ////////////////
            /*
            if(hermite==0){
                polinomio=1.0;
            }
            else if(hermite==1){
                polinomio=2*y;
            }
            else{
                polinomio=2*y;
                polinomio_antes=1.0;
                for(j=2;j<=hermite;j++){
                    ayuda=polinomio;
                    polinomio=2*y*polinomio-2*(j-1)*polinomio_antes;
                    polinomio_antes=ayuda;
                }
            }
            Phi[i]=Cgauss(0.0,polinomio*exp(-y*y/2.0));
            */
           ////////////////////////////
            Norma+=Cabs(Phi[i])*Cabs(Phi[i])*h;
        }
    }
    //Normalizo
    for(i=0;i<(N+1);i++){
        Phi[i]=Cdiv(Phi[i],Complex(sqrt(Norma),0));
    }
    //Calculo las alphas
    for(j=(N-1);j>(-1);j--){
        if(j==N-1){
            alpha[j].r=0;
            alpha[j].i=0;
        }
        else{
            alpha[j]=Cdiv(Complex(-1.0,0),Cadd(Complex(-2-Vtilde*(j*h-equilibrio)*(j*h-equilibrio),2/stilde),alpha[j+1]));
        }
    }
    k=0;
    for(n=0;n<tiempo;n=n+(ese)){//paso temporal de s
        if(k%10==0){
            cout<<n/(ese)<<endl;
            Norma=0;
            Hmedio=x2medio=xmedio=0;
            p2medio.i=pmedio.i=0;
            p2medio.r=pmedio.r=0;
            for(i=0;i<=(N);i++){//Calculo parámetros
                file_prob<<Cabs(Phi[i])*Cabs(Phi[i])*h<<"\t";
                file_real<<Phi[i].r<<"\t";
                file_img<<Phi[i].i<<"\t";


                Norma+=Cabs(Phi[i])*Cabs(Phi[i])*h;
                xmedio+=Cabs(Phi[i])*Cabs(Phi[i])*i*h*h;
                x2medio+=Cabs(Phi[i])*Cabs(Phi[i])*i*i*h*h*h;
                Hmedio+=Cabs(Phi[i])*Cabs(Phi[i])*(i*h-equilibrio)*(i*h-equilibrio);
                if(i==0){
                    pmedio=Cadd(pmedio,Cmul(Conjg(Phi[i]),Csub(Phi[i+1],Complex(0,0)))); //Oscilador armónico dentro de pozo infinito
                    p2medio=Cadd(p2medio,Cmul(Conjg(Phi[i]),Cadd(Csub(Phi[i+1],RCmul(2,Phi[i])),Complex(0,0)))); 
                }
                else if(i==N){
                    pmedio=Cadd(pmedio,Cmul(Conjg(Phi[i]),Csub(Complex(0,0),Phi[i-1])));  //Oscilador armónico dentro de pozo infinito
                    p2medio=Cadd(p2medio,Cmul(Conjg(Phi[i]),Cadd(Csub(Complex(0,0),RCmul(2,Phi[i])),Phi[i-1])));
                }
                else{
                    pmedio=Cadd(pmedio,Cmul(Conjg(Phi[i]),Csub(Phi[i+1],Phi[i-1]))); //Discretizacion del momento
                    p2medio=Cadd(p2medio,Cmul(Conjg(Phi[i]),Cadd(Csub(Phi[i+1],RCmul(2,Phi[i])),Phi[i-1]))); //Discretizacion del momento cuadrado
                }
            }
            Hmedio=Hmedio*Vtilde/h;
            pmedio=Cmul(Complex(0,-0.5),pmedio);
            p2medio=RCmul(-1.0/h,p2medio);
            Hmedio= Hmedio + p2medio.r;
            Heisenberg=sqrt(x2medio-xmedio*xmedio)*sqrt(p2medio.r-pmedio.r*pmedio.r);
            file_prob<<endl;
            file_real<<endl;
            file_img<<endl;
            file_norm<<setprecision(25)<<Norma<<endl;
            file_x<<xmedio<<endl;
            file_p<<pmedio.r<<endl;  //Error del orden h^2
            file_H<<setprecision(25)<<Hmedio<<endl;  
            file_Heisenberg<<setprecision(25)<<Heisenberg<<endl;  
        }
        for(j=(N-1);j>(-1);j--){
            if(j==(N-1)){
                beta[j].r=0;
                beta[j].i=0;
            }
            else{
                beta[j]=Cdiv(Csub(Cmul(Complex(0,4/stilde),Phi[j+1]),beta[j+1]),Cadd(Complex(-2-Vtilde*(j*h-equilibrio)*(j*h-equilibrio),2/stilde),alpha[j+1]));
            }
        }
        //creo que se podrían juntar ambas pero no estoy seguro
        for(j=0;j<(N+1);j++){
            if(j==0){
                chi[j].r=0;
                chi[j].i=0;
            }
            else{
                chi[j]=Cadd(Cmul(alpha[j-1],chi[j-1]),beta[j-1]);
                Phi[j]=Csub(chi[j],Phi[j]);
            }
        }
        k++;
    }
    cout<<"Tiempo:"<<tiempo<<endl;
    cout<<"s: (paso temporal):"<<ese<<endl;

    file_prob.close();
    file_norm.close();
    file_real.close();
    file_img.close();
    file_x.close();
    file_p.close();
    file_H.close();
    file_Heisenberg.close();
    delete[] chi;
    delete[] beta;
    delete[] alpha;
    delete[] Phi;
    return 0;
}
