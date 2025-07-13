// add underscroe and capitalize first letter of word

add_ = (str) =>{

  const fragments = str.split(" ") 
  for (let i=0 ; i<fragments.length ; i++){
      if (i==0) {
           fragments[i] = fragments[i]
continue;
}
     fragments[i] = "_" + fragments[i]
  }
      console.log(fragments.join(""))

}

add_("ui Developer role")