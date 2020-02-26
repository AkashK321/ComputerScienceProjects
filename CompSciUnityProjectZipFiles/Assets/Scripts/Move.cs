using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Move : MonoBehaviour {

    // declaring variables
    Vector3 characterScale; //used for changing direction of character based on which arrow key is clicked
    float characterScaleX; //variable for determining direction character is facing 
    public Animator anim; //animation variable
    private float MoveH; //used for horizontal movement
    private float MoveV; //used as parameter for horizontal movement
    public Rigidbody2D rb; //declaring rigid body variable
    private Vector3 Movement; //declaring movement variable, uses both MoveH and MoveV as parameters
    public float speed; //varaible to decide speed of character
    public float jumpForce; //variable to decide how high character will jump 
    bool isJumping; //variable to decide if character can jump or not
    public GameObject pauseMenuUI; //declares a game object that is linked to the pause menu game object
    public GameObject enemy; //game object for Enemy
    public GameObject enemy2; //game object for Enemy(1)
    public GameObject enemy3; //game object for Enemy(2)
    public GameObject enemy4; //game object for Enemy(3)
    public GameObject enemy5; //game object for Enemy(4)
    bool isAttacking;
    public BoxCollider2D collider1; //collider for EnemyHat
    public BoxCollider2D collider2; //collider for EnemyBody1
    public BoxCollider2D collider3; //collider for EnemyHat2
    public BoxCollider2D collider4; //collider for EnemyBody2
    public BoxCollider2D collider5; //collider for EnemyHat3
    public BoxCollider2D collider6; //collider for EnemyBody3
    public BoxCollider2D collider7; //collider for EnemyHat4
    public BoxCollider2D collider8; //collider for EnemyBody4
    public BoxCollider2D collider9; //collider for EnemyHat5
    public BoxCollider2D collider10; //collider for EnemyBody5

    // Start is called before the first frame update
    void Start()
    {
        characterScale = transform.localScale; 
        characterScaleX = characterScale.x;
        rb.freezeRotation = true; // stops character from rotating 
        anim = GetComponent<Animator>();
        pauseMenuUI.SetActive(false); // stops pause menu from being displayed
    }

    // Update is called once per frame
    void Update() {
        
        //Moving left and right
        MoveH = Input.GetAxis("Horizontal"); 
        rb.velocity = new Vector2 (speed * MoveH, rb.velocity.y);
        Movement = new Vector3(MoveH, MoveV, 0);
        rb.AddForce(Movement * speed * 10);
        
        //Changes direction character is facing based on whihc arrow key is pressed
        if (Input.GetKey("right")) {
            characterScale.x = characterScaleX;
            anim.SetTrigger("Run");
        }
        if (Input.GetKey("left")) {
            characterScale.x = -characterScaleX;
            anim.SetTrigger("Run");
        }
        else if (!Input.GetKey("left") && !Input.GetKey("right")){
            anim.SetTrigger("StopRun");
        }
        //else if (!Input.GetKey("left") && !Input.GetKey("right") && )

        Jump();

        // if escape is pressed the pause menu will be displayed and the character will be frozen
        if (Input.GetKeyDown(KeyCode.Escape)){
            Time.timeScale = 0f;
            pauseMenuUI.SetActive(true);
        }


        transform.localScale = characterScale;
    
    
    }
    //Method for jumping
    void Jump(){
            if ((Input.GetKeyDown(KeyCode.Space) || Input.GetKeyDown(KeyCode.UpArrow)) && !isJumping) {
                isJumping = true;

                rb.AddForce(new Vector2 (rb.velocity.x, jumpForce));
            }
    }
    // uses isJumping to decide if character can jump or not based on if character has collided and/or standing on sprite with tag "Ground"
    void OnCollisionEnter2D(Collision2D other){
        if(other.gameObject.CompareTag("Ground")){
            isJumping = false;

            rb.velocity = Vector2.zero; 
        }
        // if character falls of the map, the character will fall on sprite with tag "BadGround" this method will open up a new menu screen in which the player can decide to respawn or quit the game
        else if (other.gameObject.CompareTag("BadGround")){
            SceneManager.LoadScene("RespawnScene");
        }
        //system for killing enemies when jumping on their heads and beaing able to jmp again when colliding with the head of an enemy
        else if (other.collider==(collider1)){
            enemy.SetActive(false);
            isJumping = false;
        }
        else if (other.collider==collider3){
            enemy2.SetActive(false);
            isJumping = false;
        }
        else if(other.collider==collider5){
            enemy3.SetActive(false);
            isJumping = false;
        }
        else if(other.collider==collider7){
            enemy4.SetActive(false);
            isJumping = false;
        }
        else if(other.collider==collider9){
            enemy5.SetActive(false);
            isJumping = false;
        }
        //if hit body of any enemy play death animation and load respawn menu
        else if (other.collider==(collider2 || collider4 || collider6 || collider8 || collider10)){
            anim.SetTrigger("Death");
            StartCoroutine(WaitForDeath(1.25f));
        }

    }
    //waits for a certain amount of seconds and then loads the respawn scene
    IEnumerator WaitForDeath(float waitTime){
        yield return new WaitForSeconds(waitTime);
        SceneManager.LoadScene("RespawnScene");
    }

    
}
