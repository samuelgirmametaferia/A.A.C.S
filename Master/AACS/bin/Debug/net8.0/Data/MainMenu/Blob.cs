using UnityEngine;

public class Blob : MonoBehaviour
{
    public float bounceForce = 5f;

    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Wall"))
        {
            Vector2 direction = Vector2.Reflect(collision.relativeVelocity, collision.contacts[0].normal);
            GetComponent<Rigidbody2D>().velocity = direction * bounceForce;
        }
    }
}