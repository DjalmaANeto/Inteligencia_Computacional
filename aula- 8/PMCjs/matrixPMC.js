

function Matrix(linhas, colunas){
	this.linhas = linhas;
	this.colunas = colunas;
	this.matrix = [];

	for (var i = 0; i < this.linhas; i++) {
		this.matrix[i] = [];
		for (var j = 0; i < this.colunas; j++) {
			this.matrix[i][j] = 0;
		}
	}
}


Matrix.prototype.add = function(n){
	for(var i=0; i<this.linhas; i++){
		for(var j=0; j<this.colunas; j++){
			this.matrix[i][j] += n;
		}
	}
}

Matrix.prototype.multiply = function(n){
	for(var i=0; i<this.linhas; i++){
		for(var j=0; j<this.colunas; j++){
			this.matrix[i][j] *= n;
		}
	}
}