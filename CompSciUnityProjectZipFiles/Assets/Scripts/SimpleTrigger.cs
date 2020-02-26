using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class SimpleTrigger : MonoBehaviour {
    public Rigidbody2D triggerBody; // declares a 2d rigidbody object which is link to the character
    public UnityEvent onTriggerEnter; // declares a unity event object
    public GameObject LevelComplete; // declares a game object that is linkes to the level complete text game object

    // Start is called before the first frame update
    void Start(){
        // removes level complete text from display
        LevelComplete.SetActive(false);
    }
    void OnTriggerEnter2D(Collider2D other){
        //don't do anything if there is no trigger target object
        if (triggerBody == null) return;

        //only trigger if triggerBody matches
        var hitRb = other.attachedRigidbody;
        if (hitRb == triggerBody){
            // plays confetti particle effects and then displays level complete text
            onTriggerEnter.Invoke();
            LevelComplete.SetActive(true);
        }
    }
}
