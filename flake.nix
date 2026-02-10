{
  description = "Project Manager - Python DevShell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python3.withPackages (
          ps: with ps; [
            fastapi
            uvicorn
            pydantic
            pytest
          ]
        );
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [ pythonPackages ];
          shellHook = ''
            echo "Project Manager DevShell loaded"
            echo "Python version: $(python --version)"
          '';
        };
      }
    );
}
