#include "raylib.h"
#include "stdlib.h"
#include "time.h"
#include "math.h"

#define WIDTH 800
#define HEIGHT 600
#define RECT_WIDTH 10
#define RECT_HEIGHT 10

typedef struct {
    double pos_x;
    double pos_y;
    double direction;
} rect;

int main(void) {
    srand(time(NULL));

    InitWindow(WIDTH, HEIGHT, "raylib [core] example - basic window");
    SetTargetFPS(120);
    rect red_rect;
    red_rect.pos_x = 100;
    red_rect.pos_y = 100;
    red_rect.direction = (rand() % 360) * (M_PI / 180);

    while (!WindowShouldClose())
    {
        BeginDrawing();
            ClearBackground(BLACK);

            DrawRectangle(red_rect.pos_x, red_rect.pos_y, RECT_WIDTH, RECT_HEIGHT, RED);

            red_rect.pos_x += cos(red_rect.direction) * 2;
            red_rect.pos_y += sin(red_rect.direction) * 2;

            if (red_rect.pos_x > WIDTH) {
                red_rect.pos_x = WIDTH - (float)RECT_WIDTH / 2;
                red_rect.direction = (rand() % 360) * (M_PI / 180);
            } else if (red_rect.pos_x < 0) {
                red_rect.pos_x = (float)RECT_WIDTH / 2;
                red_rect.direction = (rand() % 360) * (M_PI / 180);
            }
            if (red_rect.pos_y > HEIGHT) {
                red_rect.pos_y = HEIGHT - (float)RECT_HEIGHT / 2;
                red_rect.direction = (rand() % 360) * (M_PI / 180);
            } else if (red_rect.pos_y < 0) {
                red_rect.pos_y = (float)RECT_HEIGHT;
                red_rect.direction = (rand() % 360) * (M_PI / 180);
            }
        EndDrawing();
    }
    CloseWindow();

    return 0;
}
