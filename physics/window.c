#include "raylib.h"
#include "stdlib.h"
#include "time.h"
#define _USE_MATH_DEFINES
#include "math.h"

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
#define WIDTH 800
#define HEIGHT 600
#define RECT_WIDTH 10
#define RECT_HEIGHT 10

typedef struct {
    double pos_x;
    double pos_y;
    double direction;
} rect;

void updateRectPos(rect *rect) {
    rect->pos_x += cos(rect->direction) * 2;
    rect->pos_y += sin(rect->direction) * 2;

    if (rect->pos_x > WIDTH - (float)RECT_WIDTH / 2) {
        rect->pos_x = WIDTH - (float)RECT_WIDTH / 2;
        rect->direction = (rand() % 360) * (M_PI / 180);
    } else if (rect->pos_x < (float)RECT_WIDTH / 2) {
        rect->pos_x = (float)RECT_WIDTH / 2;
        rect->direction = (rand() % 360) * (M_PI / 180);
    }
    if (rect->pos_y > HEIGHT - (float)RECT_HEIGHT / 2) {
        rect->pos_y = HEIGHT - (float)RECT_HEIGHT / 2;
        rect->direction = (rand() % 360) * (M_PI / 180);
    } else if (rect->pos_y < (float)RECT_HEIGHT / 2) {
        rect->pos_y = (float)RECT_HEIGHT;
        rect->direction = (rand() % 360) * (M_PI / 180);
    }
}

int main(void) {
    srand(time(NULL));

    InitWindow(WIDTH, HEIGHT, "raylib [core] example - basic window");
    SetTargetFPS(120);
    // red dot
    rect red_rect;
    red_rect.pos_x = rand() % WIDTH;
    red_rect.pos_y = rand() % HEIGHT;
    red_rect.direction = (rand() % 360) * (M_PI / 180);
    // green dot
    rect green_rect;
    green_rect.pos_x = rand() % WIDTH;
    green_rect.pos_y = rand() % HEIGHT;
    green_rect.direction = (rand() % 360) * (M_PI / 180);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(BLACK);

        DrawRectangle(red_rect.pos_x, red_rect.pos_y, RECT_WIDTH, RECT_HEIGHT, RED);
        DrawRectangle(green_rect.pos_x, green_rect.pos_y, RECT_WIDTH, RECT_HEIGHT, GREEN);
        updateRectPos(&red_rect);
        updateRectPos(&green_rect);

        EndDrawing();
    }
    CloseWindow();

    return 0;
}
