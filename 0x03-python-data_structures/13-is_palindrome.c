#include "lists.h"

/**
 * is_palindrome - This function checks if a singly linked list is a palindrome
 * @head: a pointer to the pointer containing the address of the first node
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *f, *s, *b, *prev;
	int length = 0, i;

	/* Check if the linked list is empty */
	if (head == NULL || *head == NULL)
		return (1);

	/* Find the middle of the linked list */
	f = s = *head;
	while (f && f->next)
	{
		f = f->next->next;
		s = s->next;
		length++;
	}

	/* Reverse the second half of the linked list */
	prev = NULL;
	b = s;

	for (i = 0; i < length; i++)
	{
		listint_t *temp = b->next;

		b->next = prev;
		prev = b;
		b = temp;
	}

	/* Compare the first and second half of the linked list */
	while (prev && *head)
	{
		if (prev->n != (*head)->n)
		return (0);
		prev = prev->next;
		*head = (*head)->next;
	}
	return (1);
}
