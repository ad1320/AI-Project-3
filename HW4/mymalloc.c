#include<stdlib.h>
#include "mymalloc.h"



typedef struct freeHeader{
    size_t size;
    struct freeHeader* next;
    struct freeHeader* prev;
}freeHeader;

typedef struct allocHeader{
    size_t size;
}allocHeader;

void* heap;
int algNum = 0;
size_t mb = 1048576;

int fits(freeHeader* current, size_t size){
    if(current->size-sizeof(freeHeader) >= size){
        return 1;
    }
    return 0;
}

void* fill(int isFirst, freeHeader* current, size_t size){
    if(isFirst){
        current += (sizeof(freeHeader))/4;
    }
    freeHeader* start = current;
    current += (sizeof(allocHeader))/4;
    void* malloc = current;
    current += size/4;
    if(size%4!=0){
        current++;
        }
    if(((uintptr_t)current)%8!=0){
        current++;
        }
    freeHeader newfree;
    newfree.prev = start;
    newfree.next = NULL;
    newfree.size = start->size-size-sizeof(freeHeader);
    freeHeader* nfp = &newfree;
    memcpy(current, nfp, sizeof(freeHeader));
    allocHeader newhdr;
    newhdr.size = size;
    allocHeader* newhdrptr = &newhdr;
    memcpy(start, newhdrptr, sizeof(allocHeader));
    
    return malloc;
    }

void myinit(int allocAlg){
    algNum = allocAlg;
    heap = malloc(mb);
    
    freeHeader start; 
    start.next = NULL;
    start.prev = NULL;
    start.size = mb;
    freeHeader* sp = &start;
    memcpy(heap, sp, sizeof(freeHeader));
    
}

void* mymalloc(size_t size){
    freeHeader* first = (freeHeader*)heap;
    freeHeader* current = first;
    while(current->next){
         current = current->next;
    }
    int isFirst = 0;
    if(current==first){
        isFirst = 1;
    }
    if(algNum==0){
        
            if(fits(current, size)){
             return(fill(isFirst, current, size));
            
        }
        printf("insufficient memory\n");
        return NULL;
    }
    else if(algNum==1){

    }
    else if (algNum==2)
    {
        /* code */
    }
    else{
        printf("invald alg number");
        return NULL;
    }
    return NULL;   
}

void mycleanup(void* ptr){
    free(ptr);
}



int main(int argc, char* argv[argc+1]){
   
    heap = malloc(mb);
    
    freeHeader start; 
    start.next = NULL;
    start.prev = NULL;
    start.size = mb;
    freeHeader* sp = &start;
    memcpy(heap, sp, sizeof(freeHeader));
    
    printf("initialized\n");

   
    
    
    char* hello = (char*)mymalloc(6*sizeof(char));
    hello[0] = 'h';
    hello[1] = 'e';
    hello[2] = 'l';
    hello[3] = 'l';
    hello[4] = 'o';
    hello[5] = '\n';
    printf("%s\n", hello);
    


    mycleanup(heap);

    return EXIT_SUCCESS;
}

