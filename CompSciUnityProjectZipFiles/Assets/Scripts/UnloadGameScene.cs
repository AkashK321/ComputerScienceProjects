using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class UnloadGameScene : MonoBehaviour
{
    // Start is called before the first frame update
    // unloads "GameScene" and "RespawnScene" so that when game starts up the other scenes are not running in the background
    void Start()
    {
        SceneManager.UnloadScene("GameScene");
        SceneManager.UnloadScene("RespawnScene");
        SceneManager.UnloadScene("PauseScene");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
