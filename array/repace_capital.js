// replace underscore and capitalize first letter of word

replace_ = (str) =>{
   const fragments = str.split("_") 
   for (let i=0 ; i<fragments.length ; i++){
      fragments[i]=  fragments[i].charAt(0).toUpperCase()+fragments[i].slice(1);
   }
      console.log(fragments.join(" "))

}

replace_("ui_developer_role")