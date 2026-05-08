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
    double x;
    double y;
    double direction;
} rect;

typedef struct {
    double x;
    double y;
} wall;

void updateRectPos(rect *rect) {
    rect->x += cos(rect->direction) * 2;
    rect->y += sin(rect->direction) * 2;

    if (rect->x > WIDTH - (float)RECT_WIDTH / 2) {
        rect->x = WIDTH - (float)RECT_WIDTH / 2;
        rect->direction = (rand() % 360) * (M_PI / 180);
    } else if (rect->x < (float)RECT_WIDTH / 2) {
        rect->x = (float)RECT_WIDTH / 2;
        rect->direction = (rand() % 360) * (M_PI / 180);
    }
    if (rect->y > HEIGHT - (float)RECT_HEIGHT / 2) {
        rect->y = HEIGHT - (float)RECT_HEIGHT / 2;
        rect->direction = (rand() % 360) * (M_PI / 180);
    } else if (rect->y < (float)RECT_HEIGHT / 2) {
        rect->y = (float)RECT_HEIGHT;
        rect->direction = (rand() % 360) * (M_PI / 180);
    }
}

int main(void) {
    srand(time(NULL));

    InitWindow(WIDTH, HEIGHT, "raylib [core] example - basic window");
    SetTargetFPS(120);
    // red dot
    rect red_rect;
    red_rect.x = rand() % WIDTH;
    red_rect.y = rand() % HEIGHT;
    red_rect.direction = (rand() % 360) * (M_PI / 180);
    // green dot
    rect green_rect;
    green_rect.x = rand() % WIDTH;
    green_rect.y = rand() % HEIGHT;
    green_rect.direction = (rand() % 360) * (M_PI / 180);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(BLACK);
        DrawRectangle(0, 0, 400, 5, RED);
        DrawRectangle(0, 50, 350, 5, RED);
        DrawRectangle(400, 0, 5, 400, RED);
        DrawRectangle(350, 50, 5, 350, RED);

        DrawRectangle(red_rect.x, red_rect.y, RECT_WIDTH, RECT_HEIGHT, RED);
        DrawRectangle(green_rect.x, green_rect.y, RECT_WIDTH, RECT_HEIGHT, GREEN);
        updateRectPos(&red_rect);
        updateRectPos(&green_rect);

        EndDrawing();
    }
    CloseWindow();

    return 0;
}
