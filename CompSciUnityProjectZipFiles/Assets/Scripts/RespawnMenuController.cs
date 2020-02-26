using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class RespawnMenuController : MonoBehaviour
{
    //public GameObject SpawnPoint;
    public Transform Spawn_Point;

    // respawns character in starting position when called
    public void Respawn(){
        SceneManager.LoadScene("GameScene");
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        player.transform.position = Spawn_Point.position;
        Time.timeScale = 1f;
        SceneManager.UnloadScene("RespawnScene");
    }

    // opens up main menu when called
    public void Quit(){
        SceneManager.LoadScene("MenuScene");
        SceneManager.UnloadScene("RespawnScene");
    }
}
