// ~~~~~~~~=============~~~~~~~~  Déclaration de variable :  ~~~~~~~~=============~~~~~~~~

// Plusieurs façon de déclarer une variable:
//Exemple 1:
var nom;
nom = "REBECCA 1";
console.log(nom);

//Exemple 2:
var nom = "REBECCA 2"; // var déclare une varible qui peut etre modifiée et re-déclarées.
var nom ="RBK";
console.log(nom);

//Exemple 3:
let surnom = "REBECCA 3"; // let déclare une variable qui peut etre modifiée mais pas re-déclarée.
console.log(surnom);

//Exemple 4:
const nom = "REBECCA 4"; // const déclare une variable qui ni ne peut être modifiées ni re-déclarées.
console.log(nom);

// Operateurs de calculs
const add = 5 + 10; // Resultat: 15
const sou = 20 - 5; // Resultat: 15
const mul = 5 * 3;  // Resultat: 15
const div = 66 / 33;// Resultat: 2

let nmb = 15;
nmb++;
nmb--;
console.log(nom);

// ==== Double guillemets et quotes ==== 
const myStr = '<a href="http://www.example.com" target="_blank">Link</a>';

/*

\'	single quote
\"	double quote
\\	backslash
\n	newline
\t	tab
\r	carriage return
\b	word boundary
\f	form feed

*/

// Concatenation des textes
let newStr = "This is the first sentence. ";
newStr += "This is the second sentence."; // Same as line 54
newStr = "This is the first sentence. " + "This is the second sentence.";
// Output : This is the first sentence. This is the second sentence.

// Exemple :
const myNoun = "dog";
const myAdjective = "big";
const myVerb = "ran";
const myAdverb = "quickly";

const wordBlanks = "The " + myAdjective + " " + myNoun + " " + myVerb + " " + myAdverb + ".";



// ~~~~~~~~=============~~~~~~~~  Longueur d'un string (.length):  ~~~~~~~~=============~~~~~~~~
// Setup
let lastNameLength = 0;
const lastName = "Lovelace";

lastNameLength = lastName.length;
// or
console.log(lastName.length);
// or
console.log("Alan Peter".length);


// ==== 1er caractere d'un String (Bracket []) ====
console.log(lastName[0])
// or
const firstName = "Charles";
const firstLetter = firstName[0];

// ==== Dernier caractere d'un String (Bracket [] + .length) ====
const lastLetterOfLastName = lastName[lastName.length-1];





// ~~~~~~~~=============~~~~~~~~  Les Tableaux / Array  ~~~~~~~~=============~~~~~~~~

// ==== Definition des Tableaux / Array : ====

// Array simple contenant INT et STRING :
const myArray = ["Mato",20,"RBK"];

// Array imbriquée :
const imbrArray = [
    ["Age",20],
    ["Prenom","Mathias"]
];

// Recupere la 1ere valeur du tableau :
const newArray = [50, 60, 70];
const myDataArray = myArray[0]

// Modifie la 1ere valeur du tableau :
myArray[0] = 45;

// Recuperer une valeur d'un tableau imbriqué :
const arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [[10, 11, 12], 13, 14]
];
const subarray = arr[3];          // subarray recupere le tableau imbriqué [[10, 11, 12], 13, 14]
const nestedSubarray = arr[3][0]; // nestedSubarray recupere le tableau [10, 11, 12]
const element = arr[3][0][1];     // element recupere le nombre 11






// ==== Manipulation des Tableaux / Array (.push)(.pop)(.shift): ====
// Push ajoute à la fin, Pop supprime à la fin, Shift supprime au debut, UnShift ajoute au debut

  const myArray = [["John", 23], ["cat", 2]];
  myArray.push(["dog", 3])
/*
De la meme facon qu'un "append", ".push" ajoute à la fin du tableau 
Ce qui forme : myArray = [["John", 23], ["cat", 2]],["dog", 3] 
*/

const threeArr = [1, 4, 6];
const oneDown = threeArr.pop(); // Recupere la valeur supprimée à la fin de l'array
console.log(oneDown);   // Affiche 6 (valeur suprimée)
console.log(threeArr);  // Affiche [1, 4] (6 Etant supprimé et stocké ailleurs)

const myArray = [["John", 23], ["dog", 3]];
const removedFromMyArray = myArray.shift(); // Recupere et Supprime de myArray la valeur au debut (["John", 23])


const myArray = [["John", 23], ["dog", 3]];
myArray.shift();               // Affichera donc myArray=[["John", 23]]
myArray.unshift(["Paul", 35]); // Affichera donc my Arrat=[["Paul", 35], ["dog", 3]]






// ~~~~~~~~=============  Les Fonctions :  =============~~~~~~~~

//Lorsqu'elle est appelée, affiche "Hi World !"
function reusableFunction() {
    console.log("Hi World !");
}
reusableFunction()

//Lorsqu'elle est appelée, additionne les arguments rentrés (1 et 2)
function functionWithArgs(int1,int2){
    console.log(int1+int2)
}  
functionWithArgs(1,2)

//Lorsqu'elle est appelée, multiplie l'argument rentré lorsqu'elle est appelée
function timesFive(int) {
    return int*5; // Le resultat est renvoyé
}
timesFive(2)



// myGlobal n'etant pas dans une fonction est forcement globale et recuperable par toutes les fonctions
const myGlobal = 10;

function fun1() {
  // Variable déclarée sans let ou const: FORCEMENT en global scope (utilisable partout)
  oopsGlobal = 5
};

// Only change code above this line

function fun2() {
  let output = "";
  if (typeof myGlobal != "undefined") {
    output += "myGlobal: " + myGlobal;
  }
  if (typeof oopsGlobal != "undefined") {
    output += " oopsGlobal: " + oopsGlobal;
  }
  console.log(output);
};