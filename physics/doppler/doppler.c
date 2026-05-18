#include <raylib.h>

#define WIDTH 800
#define HEIGHT 600
#define MAX_CIRCLES 250

struct Circle {
    int x,y;
    float r;
};

struct Circle circle;
struct Circle circles[MAX_CIRCLES];
int circle_n = 0;
int px = WIDTH/2;
int py = HEIGHT/2;

void create_waves(int x, int y) {
    for (int i = 0; i < MAX_CIRCLES; i++) {
        circles[i] = (struct Circle){x, y, 0};
    }
}

void draw_waves() {
    DrawCircleLines(circles[circle_n].x, circles[circle_n].y, circles[circle_n].r+(circle_n*2), WHITE);
    circle_n++;
    if (circle_n == MAX_CIRCLES - 1) circle_n = 0;
}

int main(void) {
    InitWindow(WIDTH, HEIGHT, "Doppler");
    SetTargetFPS(60);
    float interval = 0;
    float dt;
    circle = (struct Circle){px, py, 0};
    while (!WindowShouldClose()) {
        if (IsKeyDown(KEY_UP)) circle.y -= 2;
        if (IsKeyDown(KEY_DOWN)) circle.y += 2;
        if (IsKeyDown(KEY_RIGHT)) circle.x += 2;
        if (IsKeyDown(KEY_LEFT)) circle.x -= 2;
        DrawCircle(circle.x, circle.y, 50, WHITE);
        dt = GetFrameTime();
        interval += dt;
        BeginDrawing();
        ClearBackground(BLACK);
        if (interval > 1.0f) {
            create_waves(circle.x, circle.y);
            draw_waves();
        }
        EndDrawing();
    }
    CloseWindow();
}
