using UnityEngine;

public class Wall : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Blob"))
        {
            // Handle collision with blob, e.g., game over
        }
    }
}