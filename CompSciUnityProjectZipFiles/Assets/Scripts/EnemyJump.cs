using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyJump : MonoBehaviour
{
    public float jumpForce; //variable for jump force
    public Rigidbody2D rb; //rigidbody variable for enemy
    public GameObject ob; //game object variable for enemy
    private float MoveH; //variable for horizontal movement, used for jumping
    private float speed; //variable for speed, used for jumping
    // Start is called before the first frame update
    void Start()
    {
        MoveH = Input.GetAxis("Horizontal");
        ob.GetComponent<Rigidbody2D>().constraints = RigidbodyConstraints2D.FreezePositionX; //stops enemy from moving left and right
        rb.freezeRotation = true; //stops enemy from rotating
    }

    // Update is called once per frame
    void Update()
    {
        rb.velocity = new Vector2(speed * MoveH, rb.velocity.y);
    }
    //enemy will jump if on ground
    void OnCollisionEnter2D(Collision2D other){
        if(other.gameObject.CompareTag("Ground")){
            rb.AddForce(new Vector2 (rb.velocity.x, jumpForce));
        }
    }
}
