export class Linear {
  name: string;
  series: Array<{ name: string, value: string }>;

  constructor(name: string, series: Array<{ name: string; value: string }>) {
    this.name = name;
    this.series = series;
  }
}
