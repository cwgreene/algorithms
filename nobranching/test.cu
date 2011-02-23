#include <stdio.h>
#include <time.h>
#include <stdlib.h>

__global__ void kernelDoom(int *a)
{
	int i = blockIdx.x*blockDim.x+threadIdx.x;
	/*Branch Version*/
	for(int k =0; k < 100;k++)
	{
		if(a[i]>=0)
			a[i] = a[i]+1;
		else
			a[i] = a[i]-1;	
	}
}

__global__ void nobranchDoom(int *a)
{
	int i = blockIdx.x*blockDim.x+threadIdx.x;
	for(int k = 0; k < 100;k++)
	a[i] = a[i] + (1+2*((a[i] & -1)>>31));
}


#define SAFE_CUDA(call) \
printf("calling: "#call "\n");\
err=call;\
printf(#call ": %d %d\n",err,cudaSuccess);

#define TIME_IT(name,x) \
SAFE_CUDA(cudaMemcpy(nums_d,o_nums,size,cudaMemcpyHostToDevice));\
printf(#x"\n");\
start = clock();\
x;\
SAFE_CUDA(cudaMemcpy(nums,nums_d,size,cudaMemcpyDeviceToHost));\
end = clock();\
printf("clocks "#name ": %d\n",end-start);\
printf("\n\n");



int main()
{	
	int N = 512*512;
	printf("starting\n");
	size_t size = N*sizeof(int);
	int *o_nums = (int *)malloc(size);
	int *nums = (int *)malloc(size);
	int *nums_d;
	int err = 0;
	int start,end;

	printf("beginning cuda alloc\n");
	SAFE_CUDA(cudaMalloc(&nums_d,size));
	for(int i =0;i< N;i++)
		o_nums[i] = i*(1-2*(random()%2));

	TIME_IT(kerneldoom,(kernelDoom<<<512,512>>>(nums_d)));
	
//	TIME_IT(nobranch, (nobranchDoom<<<512,512>>>(nums_d)));

//	TIME_IT(kerneldoom,(kernelDoom<<<512,512>>>(nums_d)));


	cudaFree(nums_d);
}
