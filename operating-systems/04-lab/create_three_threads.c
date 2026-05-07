#include <pthread.h>
#include <stdio.h>

void* thread_function(void* arg) {
    printf("Thread %ld running\n", (long)arg);
    return NULL;
}

int main() {
    pthread_t threads[3];
    for (long i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, thread_function, (void*)i);
    }
    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
