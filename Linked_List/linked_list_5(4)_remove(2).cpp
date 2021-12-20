#include <stdio.h>

int main(){
}

struct node{
  char *data;
  struct node *next; // 다음 노드의 주소를 저장할 필드이다. 이렇게 자신과 동일한 구조체에 대한 포인터를 멤버로 가진다는 의미에서 "자기참조형 구조체"라고 부르기도 한다.
};

typedef struct node Node;
Node *head = NULL; // 연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.

// 입력된 스트링을 저장한 노드를 찾아 삭제한다. 삭제된 노드에 저장된 스트링을 반환한다.
// 삭제할 노드를 찾아도 해당 노드를 삭제하기 위해서는 삭제할 노드가 아니라 직전 노드의 주소가 필요하다. 따라서 두 개의 포인터가 필요하다.
Node *remove(char *item){
  Node *p = head;
  Node *q = NULL;
  while (p!=NULL && strcmp(p->data, item)!=0){
    q = p; // q는 항상 p의 직전 노드를 가리킨다. p가 첫번째 노드일 경우 q는 NULL이다.
    p = p->next;
  }

  if (p==NULL)
    return NULL;
  if (q==NULL)
    return remove_first();
  else
    return remove_after(q);
}
