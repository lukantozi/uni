#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

void *thread_function(void *arg) {
    for (int i = 1; i <= 5; i++) {
        printf("Thread running: iteration %i\n", i);
        sleep(1);
    }
    return 0;
}

int main() {
    pthread_t thread_id;
    pthread_create(&thread_id, NULL, thread_function, NULL);
    pthread_join(thread_id, NULL);
    return 0;
}
