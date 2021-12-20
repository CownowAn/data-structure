#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 연결리스트 순회하기(traverse)
Node *find(char *word){
  Node *p = head;
  while (p != NULL){
    if (strcmp(p->data, word) == 0)
      return p;
    p = p->next;
  }
  return NULL;
}
/* 연결리스트의 노드들을 처음부터 순서대로 방문하는 것을 순회(traverse)한다고 말한다. 
이 함수는 입력된 문자열 word와 동일한 단어를 저장한 노드를 찾아서 그 노드의 주소를 반환한다. 
그것을 위해서 연결리스트를 순회한다. */
