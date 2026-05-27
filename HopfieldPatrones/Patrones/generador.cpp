#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include <sstream>
#include <random>
#include <chrono>



using namespace std;



int main(){
    int i, j;
    int N=4900;
    int numero=100;
    unsigned int seed1 = chrono::system_clock::now().time_since_epoch().count();

    mt19937_64 generator(seed1);
    uniform_real_distribution<double> r_distribution(0., 1.);

    ofstream patron("aleatorio.txt");

    if(!patron){
       cout<<"Error al abrir el archivo."<<endl;
       return 1;
    }
    for(j=0;j<numero;j++){
        for(i=0;i<(N-1);i++){
            if(r_distribution(generator)<=0.5)
                patron<<1<<"\t";
            else
                patron<<0<<"\t";
        }
        patron<<endl;
    }

    patron.close();
    return 0;
}