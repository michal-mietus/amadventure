console.log(abilities)

function displayAbilities(abilities){
    for(var branch=0; branch<abilities.length; branch++){
        console.log(abilities[branch]);
        for (var ability=0; ability<abilities[branch].length; ability++){
            console.log(abilities[branch][ability]);
        };
    };
}

function createBranchContainers(abilites){
    for(var branch=0; branch<abilities.length; branch++){
        let div = document.createElement('div');
        div.className = 'branch ' + branch;
        container = document.getElementById('field-container');
        container.appendChild(div);
    };
}

function moveAbilitiesToSeparateBranchDivs(abilities){
    for(var branch=0; branch<abilities.length; branch++){
        for (var ability=0; ability<abilities[branch].length; ability++){
            field_div = document.getElementById(abilities[branch][ability].name);
            branch_div = document.getElementsByClassName('branch ' + branch)[0];
            branch_div.appendChild(field_div);
        };
    };
}

function createNodesAndTrees(abilities){
    trees = [];
    for(var branch=0; branch<abilities.length; branch++){
        let branchTree = new AbilitiesTree(branch);
        for (var ability=0; ability<abilities[branch].length; ability++){
            if (abilities[branch][ability].parent == null){
                node = new Node(abilities[branch][ability]);
                branchTree.setRoot(node);
            } else {
                let node = new Node(abilities[branch][ability]);
                branchTree.addNode(node);
            };
        };
        trees.push(branchTree);
    };
    return trees;
}

class Node {
    constructor(ability){
        this.ability = ability;
        this.childs = [];
    };

    addChild(ability){
        this.childs.push(ability);
    };
};

class AbilitiesTree {
    constructor(branch){
        this.root = null;
        this.nodes = [];
        this.branch = branch;
    };

    setRoot(node){
        this.root = node;
    };

    addNode(node){
        this.nodes.push(node);
    };

    findNode(ability_name){
        for (var i=0; i<this.nodes.length; i++){
            if(this.nodes[i].ability.name == ability_name) {
                console.log('node');
                return this.nodes[i];
            } else if(ability_name == this.root.ability.name){
                console.log('root');
                return this.root;
            }
            ;
        };
    };

    findNodes(ability_name){
        let found_nodes = [];
        for (var i=0; i<this.nodes.length; i++){
            if(this.nodes[i].ability.name == ability_name) {
                found_nodes.push(this.nodes[i]);
            };
        };
        return found_nodes;
    };

    findChilds(){
        for (var i=0; i<this.nodes.length; i++){
            if (this.nodes[i].ability.parent != null){
                console.log('parent', this.nodes[i].ability.parent);
                parent = this.findNode(this.nodes[i].ability.parent);
                parent.addChild(this.nodes[i]);
            };
        };
    };

    createDivAndMoveChilds(node){
        branch_element = document.getElementsByClassName(this.branch)[0];
        div = document.createElement('div');
        child_elements = []
        for(var i=0; i<node.childs.length; i++){
            child_field = document.getElementById(node.childs[i].ability.name);
            child_elements.push(child_field);
        };
        // create container for childs and move them there.
    };
};


createBranchContainers(abilities);
moveAbilitiesToSeparateBranchDivs(abilities);
trees = createNodesAndTrees(abilities);
for(var i=0; i<trees.length; i++){
    trees[i].findChilds();
}
console.log(trees);