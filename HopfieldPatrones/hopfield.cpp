#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include <sstream>
#include <random>
#include <chrono>

using namespace std;



int main()
{
    ///Declarar variables
    int i,j,tiempo,k, ayuda; //Variables de iteración
    int N=4900, iteraciones=4900*30; //Variables dependientes del sistema, N es el número de celdas, 10^3 pasos montecarlo
    //int orden=0 ,x=0;  //Variables del generador semilla=x
    //unsigned int seed1 = chrono::system_clock::now().time_since_epoch().count();//genero semilla aleatoria(dependiente del tiempo en el que ejecute)
    unsigned int seed1 = 389458993;  //genero numero aleatorios a partir de una semilla para poder replicar resultados
    int n,m; //Variables de localizador de celdas
    double T=1.0,p,exponencial;     //Valores de T entre 0 y 5
    int P=3;  //Numero de patrones
    double a[P], w, epsilon=1e-10;
    double normalizar[P];
    double* solapamiento = new double[P];
    string linea;
    int* s = new int[N];
    int** patron = new int*[P];
    for (i=0;i<P;i++){
        patron[i]= new int[N];
    }
    

    mt19937_64 generator(seed1);
    uniform_real_distribution<double> r_distribution(0., 1.);


    ofstream archivo("Datos/Datos.txt");

    if(!archivo){
       cout<<"Error al abrir el archivo Datos."<<endl;
       return 1;
    }

    ofstream solo("Solapamiento/Solapamiento.txt");

    if(!solo){
       cout<<"Error al abrir el archivo Solapamiento."<<endl;
       return 1;
    }

    ifstream patronuno("Imagenes/Newton.txt");

    if(!patronuno){
      cout<<"Error al abrir el archivo 1."<<endl;
       return 1;
    }

    //Leo el archivo y quito la primera columna
    i=0;
    while (getline(patronuno,linea)){
        stringstream ss(linea);

        string basura;
        ss >> basura;

        while(ss >> ayuda){
            if (i >= N) break;
            patron[0][i]=ayuda/255;
            i++;
        }
    }
    patronuno.close();

    

    ifstream patrondos("Imagenes/Maxwell.txt");

    if(!patrondos){
       cout<<"Error al abrir el archivo 2."<<endl;
       return 1;
    }

    //Leo el archivo y quito la primera columna
    i=0;
    while (getline(patrondos,linea)){
        stringstream ss(linea);

        string basura;
        ss >> basura;

        while(ss >> ayuda){
            if (i >= N) break;
            patron[1][i]=ayuda/255;
            i++;
        }
    }
    patrondos.close();


    ifstream patrontres("Imagenes/Einstein.txt");

    if(!patrontres){
       cout<<"Error al abrir el archivo 3."<<endl;
       return 1;
    }

    //Leo el archivo y quito la primera columna
    i=0;
    while (getline(patrontres,linea)){
        stringstream ss(linea);

        string basura;
        ss >> basura;

        while(ss >> ayuda){
            if (i >= N) break;
            patron[2][i]=ayuda/255;
            i++;
        }
    }
    patrontres.close();
    


    
    //Estado Inicial Patron difuso   0=Newton  1=Maxwell  2=Einstein
    
    for(i=0;i<N;i++){
        s[i]=patron[1][i];
        if(r_distribution(generator)<=0.2){//Cambio un 20% del patron alterado
            if(r_distribution(generator)<=0.5)
                s[i] = 1;
            else
                s[i]=0;
        }
    }
    
    //Estado Inicial Patrón Aleatorio
    /*
    for(i=0;i<N;i++){
        if(r_distribution(generator)<=0.5)
            s[i] = 1;
        else
            s[i]=0;
    }
    */
    //Definiendo el parámetro a y la normalización
    for(i=0;i<P;i++){
        a[i]=0;
        for (j = 0; j < N; j++)
        {
            a[i]+=patron[i][j];
        }
        a[i]=a[i]/(N);
        normalizar[i]=a[i]*(1-a[i]);
    }
    


     
  
        for(tiempo=0;tiempo<iteraciones;tiempo++){
            n=r_distribution(generator)*(N);   //alterar límites de la distribución Distribución uniforme [0,1]
            
            exponencial=0;
            for(m=0;m<N;m++){ //interacción de todas las neuronas con la neurona n
                w=0;
                for(k=0;k<P;k++){
                    w+=(patron[k][n]-a[k])*(patron[k][m]-a[k]);  
                }
                w=w/(N);
            
                if(n==m){
                    exponencial+=0;
                }
                else{
                    if(s[n]==1){
                        exponencial+=(2*w*s[m]-w);
                    }
                    else{
                        exponencial-=(2*w*s[m]-w);
                    }
                }
            }



            if(T==0){//Caso límite T=0, depende únicamente del signo de de la variación de energía
                if(exponencial>0){
                    exponencial=0;
                }
                else if(exponencial<=0){
                    exponencial=1;
                }
            }
            else{
                exponencial=exp(-exponencial/(T));
            }



            //Algoritmo de rechazo por metrópolis
            if (1<exponencial){
                p=1;
            }
            else{
                p=exponencial;
            }
            if (r_distribution(generator)<p){
                s[n]=abs(s[n]-1);
            }
            if(tiempo%(N)==0){//Guardar cada paso Montecarlo
                for(i=0;i<N;i++){
                    archivo<<s[i]<<"\t";
                }
                archivo<<endl;
                //Para controlar el progreso del codigo
                //cout<<"Iteracion de 200: "<<(tiempo/N)<<endl;
                for(i=0;i<P;i++){
                    solapamiento[i]=0;
                    for(j=0;j<N;j++){
                        solapamiento[i]+=(patron[i][j]-a[i])*(1.0*s[j]-a[i]);
                    }
                    solapamiento[i]=solapamiento[i]/(N*normalizar[i]);
                    solo<<solapamiento[i]<<"\t";
                }
                solo<<endl;
            }
            
            
        }



    for(i=0;i<P;i++){
        delete[] patron[i];
    }
    delete[] patron;
    delete[] solapamiento;
    delete[] s;
    archivo.close();
    solo.close();
    return 0;
}