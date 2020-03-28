export class Linear {
  name: string;
  series: Array<Series> = [];

  constructor(name: string) {
    this.name = name;
  }
}

export class Series {
  name: string;
  value: number;

  constructor(name: string, value: number) {
    this.name = name;
    this.value = value;
  }
}
