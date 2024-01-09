#include "lists.h"
#include <stdio.h>

/**
* list_len - prints all elemnets in list
* @h: pointer to struct node
* Return: int count
*/
size_t list_len(const listint_t *h)
{
	size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
/**
 * is_palindrome - check if linked list is palindrome
 * @head: address of pointer to head
 * Return: int 1 on if palindrome 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev, *tmp;

	if (list_len(*head) == 0)
		return (1);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	prev = slow, slow = slow->next, prev->next = NULL;
	while (slow)
	{
		tmp = slow->next, slow->next = prev, prev = slow, slow = tmp;
	}
	fast = *head, slow = prev;
	while (slow)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next, slow = slow->next;
	}
	return (1);
}
