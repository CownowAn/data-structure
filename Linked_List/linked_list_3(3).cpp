#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 연결리스트의 맨 앞에 새로운 노드 삽입하는 함수 (첫 번째 노드를 가리키는 포인터 head가 전역변수가 아닌 경우)
// **ptr_head는 포인터 변수 head의 주소를 매개변수로 받기 위함이다.
void add_first(Node **ptr_head, char *item){
  Node *temp = (Node *)malloc(sizeof(Node));
  temp->data = item;
  temp->next = *ptr_head;
  *ptr_head = temp; // 바뀐 head 노드의 주소를 포인터를 이용하여 변수 head에 쓴다.
}
// 이렇게 구현할 경우 이 함수는 다음과 같이 호출해야 한다.
// add_first(&head, item_to_store);
