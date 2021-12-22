#include <stdlib.h>

struct term {
    int coef;
    int expo;
    struct term *next;
};
typedef struct term Term;

typedef struct polynomial {
    char name;
    Term *first;
    int size = 0;
} Polynomial;

Polynomial *polys[MAX_POLYS]; // polys는 다항식들에 대한 포인터들의 배열이다.
int n = 0; // 저장된 다항식들의 개수

/* 동적으로 생성된 객체를 적절하게 초기화해주지 않는 것이 종종 프로그램의 오류를 야기한다.
이렇게 객체를 생성하고 기본값으로 초기화해주는 함수를 따로 만들어 사용하는 것은 좋은 프로그래밍 방법이다. */
Term *creat_term_instance() {
    Term *t = (Term *)malloc(sizeof(Term));
    t->coef = 0;
    t->expo = 0;
    return t;
}
// Polynomial 객체 생성 시, 이름을 지정해주도로 만들었다.
Polynomial *creat_polynomial_instance(char name) {
    Polynomial *ptr_poly = (Polynomial *)malloc(sizeof(Polynomial));
    ptr_poly->name = name;
    ptr_poly->size = 0;
    ptr_poly->first = NULL;
    return ptr_poly;
}

// 항을 추가하는 함수
void add_term(int c, int e, Polynomial *poly) {
    if (c==0)
        return;
    
    Term *p = poly->first, *q = NULL;
    while (p!=NULL && p->expo > e) {
        q = p;
        p = p->next;
    }
    if (p!=NULL && p->expo==e) { // 동일 차수의 항이 존재하는 경우
        p->coef += c;
        if (p->coef == 0){ // 더했더니 계수가 0이 되는 경우
            // q의 다음 노드를 삭제시킨다. 단 q가 NULL이면 첫 번째 노드를 삭제한다.
            if (q == NULL)
                poly->first = p->next;
            else
                q->next = p->next;
            poly->size--;
            free(p); // 불필요해진 노드 p를 free시킨다.
        }
    }
    return;

    // 동일 차수의 항이 존재하지 않는 경우, 새로운 Term 생성
    Term *term = creat_term_instance();
    term->coef = c;
    term->expo = e;

    if (q==NULL) { // 맨 앞에 삽입하는 경우
        term->next = poly->first;
        poly->first = term;
    }
    else { // q의 뒤, p의 앞에 삽입하는 경우(p는 NULL일 수도 있다.)
        term->next = p;
        q->next = term;
    }
    poly->size++;
}

// 다항식의 값을 계산하는 함수
int eval(Polynomial *poly, int x) {
    int result = 0;
    Term *t = poly->first;
    while (t!=NULL) {
        result += eval(t, x); // 각각의 항의 값을 계산하여 더한다.
        t = t->next;
    }
    return result;
}

int eval(Term *term, int x) { // 하나의 항의 값을 계산하는 함수
    int result = term->coef;
    for (i=0; i<term->expo; i++) {
        result *= x;
    }
    return result;
}

// 다항식을 출력하는 함수
void print_poly(Polynomial *p) {
    printf("%c=", p->name);
    Term *t = p->first;
    while (t!=NULL) {
        print_term(t);
        printf("+");
        t = t->next;
    }
}

void print_term(Term *pTerm) {
    printf("%dx^%d", pTerm->coef, pTerm->expo);
}

// 사용자의 명령을 받아 처리하는 함수
void process_command() {
    
    char command_line[BUFFER_LENGTH];
    char copied[BUFFER_LENGTH];
    char *command, *arg1, *arg2;

    while(1) {
        printf("$ ");
        if (read_line(stdin, command_line, BUFFER_LENGTH) <= 0)
            continue;
        strcpy(copied, command_line);
        command = strtok(command_line, " ");
        if (strcmp(command, "print")==0) {
            arg1 = strtok(NULL, " ");
            if (arg1==NULL) {
                printf("Invalid arguments.\n");
                continue;
            }
            handle_print(arg1[0]);
        }
        else if (strcmp(command, "calc")==0) { // ex) calc f 1
            arg1 = strtok(NULL, " ");
            if (arg1 == NULL) {
                printf("Invalid arguments.\n");
                continue;
            }
            arg2 = strtok(NULL, " ");
            if (arg2 == NULL) {
                printf("Invalid arguments.\n");
                continue;
            }
            handle_calc(arg1[0], arg2);
        }
        else if (strcmp(command, "exit")==0)
            break;
        else {
            handle_definition(copied) // 다항식을 입력받아 정의하는 일을 한다.
        }
    }
}
