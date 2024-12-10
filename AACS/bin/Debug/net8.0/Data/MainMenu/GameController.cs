using UnityEngine;

public class GameController : MonoBehaviour
{
    public GameObject blob;
    public float blobSpeed = 5f;

    void Update()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(horizontalInput, verticalInput, 0);
        blob.transform.Translate(movement * blobSpeed * Time.deltaTime);
    }
}