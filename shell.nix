{ pkgs ? import <nixpkgs> { } }:

let
  myOpenai = ps:
    with ps;
    [
      (buildPythonPackage rec {
        pname = "openai";
        version = "0.27.9";
        src = fetchPypi {
          inherit pname version;
          sha256 = "sha256-tod2HIL167b2Hvx5GyCD0tBoJ3uUgC1NE2nv45hRgT0=";
        };
        doCheck = false;
        propagatedBuildInputs = [
          pkgs.python3Packages.tqdm
          pkgs.python3Packages.requests
          pkgs.python3Packages.aiohttp
        ];
      })
    ];
in pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.python-dotenv
    (python3.withPackages myOpenai)
  ];
}
