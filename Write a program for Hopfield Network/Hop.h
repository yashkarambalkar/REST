#include <stdio.h>
#include <iostream.h>
#include <math.h>
class neuron
{
protected:
	int activation;
	friend class network;
public:
	intweightv[4];
	neuron() {};
	neuron(int *j) ;
	int act(int, int*);
};
class network
{
public:
	neuron nrn[4];
	int output[4];
	intthreshld(int) ;
	void activation(int j[4]);
	network(int*,int*,int*,int*);
};