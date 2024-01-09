#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
size_t list_len(const listint_t *h);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
